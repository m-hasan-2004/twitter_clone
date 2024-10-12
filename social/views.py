from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from users.models import User
from .forms import CreateCommentForm, CreatePostForm
from .models import Post, Like, Follow, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

class ExploreView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, 'social/explore.html', context=context)

    def post(self, request):
        # Handling likes
        post_id = request.POST.get("post_id")
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            liked = Like.objects.filter(user=request.user, post=post).exists()

            if liked:
                Like.objects.filter(user=request.user, post=post).delete()
            else:
                Like.objects.create(user=request.user, post=post)

        # Handling follows
        follow_id = request.POST.get("follow_id")
        if follow_id:
            follow_user = get_object_or_404(User, id=follow_id)  # Adjust as necessary

            followed = Follow.objects.filter(follower=request.user, following=follow_user).exists()

            if followed:
                Follow.objects.filter(follower=request.user, following=follow_user).delete()
            else:
                Follow.objects.create(follower=request.user, following=follow_user)

        # Redirect back to explore page
        return redirect('social:explore')
    
    
class CreateAndExploreCommentsView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)  # Fetch the post using UUID
        comments = post.comments.all()  # Get all comments for the post
        form = CreateCommentForm()  # Create an empty form instance

        return render(request, "social/createandexplorecomments.html", {
            "post": post,
            "comments": comments,
            "form": form,
        })

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        author = request.user

        # Check if the post request is for comment deletion
        if 'delete_comment_id' in request.POST:
            comment_id = request.POST.get('delete_comment_id')
            comment = get_object_or_404(Comment, id=comment_id, post=post, author=author)
            comment.delete()
            return redirect('social:comments', post_id=post.id)

        # Otherwise, process the form submission for new comments
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = author
            new_comment.save()

            return redirect('social:comments', post_id=post.id)

        comments = post.comments.all()
        return render(request, "social/createandexplorecomments.html", {
            "post": post,
            "comments": comments,
            "form": form,
        })


class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        # Render a blank form for creating a post
        form = CreatePostForm()
        return render(request, 'social/create_post.html', {'form': form})

    def post(self, request):
        # Handle the post submission
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new post but don't save it yet
            new_post = form.save(commit=False)
            # Assign the author of the post to the logged-in user
            new_post.author = request.user
            # Save the post
            new_post.save()
            # Redirect to some page, e.g., the explore page or post details
            return redirect('social:explore')
        # If the form is invalid, re-render the page with form errors
        return render(request, 'social/create_post.html', {'form': form})
    

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('social:explore')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, 'Post deleted successfully.')
        return HttpResponseRedirect(success_url)
