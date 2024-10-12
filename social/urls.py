from django.urls import path
from .views import ExploreView, CreateAndExploreCommentsView, CreatePost, DeletePostView, EditPostView

app_name = 'social'

urlpatterns = [
    path('explore/', ExploreView.as_view(), name="explore"),
    path("comments/<uuid:post_id>", CreateAndExploreCommentsView.as_view(), name="comments"),
    path("create_post/", CreatePost.as_view(), name="create_post"),
    path('post/<uuid:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path("edit_post/<uuid:pk>", EditPostView.as_view(), name="edit_post"),
]
