from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .forms import ProfileForm, PasswordChangeForm, CustomUserCreationForm, ProfilePicChangeForm
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import os


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:account_settings')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.pic = form.cleaned_data.get('pic')
        return super().form_valid(form)
    

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:account_settings')


class AccountSettingsView(LoginRequiredMixin, View):
    template_name = 'users/account_settings.html'
    success_url = reverse_lazy('users:account_settings')

    def get(self, request, *args, **kwargs):
        profile_form = ProfileForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
        profile_pic_form = ProfilePicChangeForm(instance=request.user)

        return render(request, self.template_name, {
            'form_profile': profile_form,
            'form_password': password_form,
            'form_profile_pic': profile_pic_form,
        })

    def post(self, request, *args, **kwargs):
        profile_form = ProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        profile_pic_form = ProfilePicChangeForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect(self.success_url)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully.')
            return redirect(self.success_url)
        
        if profile_pic_form.is_valid():
            profile_pic_form.save()
            messages.success(request, "Your profile picture has been updated successfully.")
            return redirect(self.success_url)

        # If neither form is valid, re-render with errors
        return render(request, self.template_name, {
            'form_profile': profile_form,
            'form_password': password_form,
            'form_profile_pic': profile_pic_form,
        })


class DeleteAccountView(LoginRequiredMixin, View):
    success_url = reverse_lazy('core:home')

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.pic and os.path.isfile(os.path.join(settings.MEDIA_ROOT, str(user.pic))):
            try:
                # Remove the profile picture from the filesystem
                os.remove(os.path.join(settings.MEDIA_ROOT, str(user.pic)))
            except Exception as e:
                messages.error(request, f"Error deleting profile picture: {str(e)}")
        user.delete()
        messages.success(request, "Your account has been deleted successfully.")
        return redirect(self.success_url)
    