from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import PasswordChangeForm


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
        return self.render_to_response(self.get_context_data(password_form=password_form, email_form=email_form))

    def post(self, request, *args, **kwargs):
        password_form = PasswordChangeForm(user=self.request.user, data=request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, 'Your email and password have been updated successfully!')
            return self.form_valid(password_form)

        return self.form_invalid(password_form)


