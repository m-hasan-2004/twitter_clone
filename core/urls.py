from django.urls import path
from .views import HomeView

app_name = 'core'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]

handler404 = "core.views.custom_404"