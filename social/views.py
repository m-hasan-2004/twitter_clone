from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import models # to be


class ExploreView(View):
    def get(self, request):
        return render(request, 'social/explore.html')