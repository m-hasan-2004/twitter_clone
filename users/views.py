from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileForm, PasswordChangeForm

@login_required
def account_settings(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('users:account_settings')

        if password_form.is_valid():
            password_form.save()
            return redirect('users:account_settings')


    else:
        profile_form = ProfileForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'users/account_settings.html', {
        'form_profile': profile_form,
        'form_password': password_form,
    })