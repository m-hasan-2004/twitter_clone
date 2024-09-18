from django.urls import path
from .views import account_settings
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('account_settings/', account_settings, name="account_settings")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)