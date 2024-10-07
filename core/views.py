from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')
    

def custom_404(request, exception=None):
    return render(request, 'core/404.html', status=404)