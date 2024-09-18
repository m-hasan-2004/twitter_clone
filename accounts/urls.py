from django.urls import path
from .views import SignupView, CustomLoginView, AccountSettingsView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

# accounts/urls.py


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('account_settings/', AccountSettingsView.as_view(), name='account_settings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)