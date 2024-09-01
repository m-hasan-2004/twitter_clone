from django.urls import path
from .views import AccountSettingsView

app_name = 'users'

urlpatterns = [
    path('account_settings/', AccountSettingsView.as_view(), name="account_settings")
]
