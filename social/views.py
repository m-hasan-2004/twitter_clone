from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from users.models import User
from .models import Post, Like, Follow
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