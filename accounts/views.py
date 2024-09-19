from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.views import View


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('users:account_settings')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# accounts/views.py


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('admin/')


# accounts/views.py
class AccountSettingsView(LoginRequiredMixin, FormView):
    template_name = 'users/account_settings.html'
    success_url = reverse_lazy('account_settings')

    def get(self, request, *args, **kwargs):
        password_form = PasswordChangeForm(user=self.request.user)
        return self.render_to_response(self.get_context_data(password_form=password_form))

    def post(self, request, *args, **kwargs):
        password_form = PasswordChangeForm(user=self.request.user, data=request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your email and password have been updated successfully!')
            return self.form_valid(password_form)

        return self.form_invalid(password_form)


class DeleteAccountView(LoginRequiredMixin, View):
    success_url = reverse_lazy('core:home')

    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted successfully.")
        return redirect(self.success_url)
    


