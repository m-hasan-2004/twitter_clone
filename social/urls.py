from django.urls import path
from .views import ExploreView, CreateAndExploreCommentsView

app_name = 'social'

urlpatterns = [
    path('explore/', ExploreView.as_view(), name="explore"),
    path("comments/<uuid:post_id>", CreateAndExploreCommentsView.as_view(), name="comments")
]

