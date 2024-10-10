from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from users.models import User
from .forms import CreateCommentForm
from .models import Post, Like, Follow, Comment
from django.contrib.auth.mixins import LoginRequiredMixin 

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
