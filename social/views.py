from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post, Like, Follow
from django.contrib.auth.mixins import LoginRequiredMixin 

class ExploreView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, 'social/explore.html', context=context)

    def post(self, request):
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        
        # Check if the user has already liked the post
        liked = Like.objects.filter(user=request.user, post=post).exists()

        if liked:
            # If liked, remove the like (unlike)
            Like.objects.filter(user=request.user, post=post).delete()
        else:
            # Otherwise, create a new like
            Like.objects.create(user=request.user, post=post)

        # After processing the like, reload the page to reflect changes
        return redirect('social:explore')
