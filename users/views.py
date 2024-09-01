from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.

class AccountSettingsView(View):
 
    def get(self, request, id):
        account = get_object_or_404(id=id)
        context = {"account": account}
        return render(request=request, template_name="accounts/accounts_settings.html", context=context) 