from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Like, Follow


class ExploreView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts,}
        return render(request, 'social/explore.html', context=context)