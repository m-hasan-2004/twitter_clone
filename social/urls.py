from django.urls import path
from .views import ExploreView

app_name = 'social'

urlpatterns = [
    path('explore/', ExploreView.as_view(), name="explore")
]

