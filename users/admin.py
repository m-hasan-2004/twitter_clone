from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    readonly_fields = ('id', 'last_login', 'date_joined')
    save_on_top = True
    ordering = ('-date_joined', 'username')
    list_per_page = 25

    fieldsets = (
        ("Login Info", {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'pic')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Override the form used to change the password in the admin
    change_password_form = AdminPasswordChangeForm

    # Ensure the password is hashed correctly
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            # Hash the password if it's being changed or set
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        """Return different fieldsets depending on whether the object is being created or edited."""
        if not obj:
            # When creating a user, you need to provide the password twice
            return (
                ("Login Info", {
                    'fields': ('username', 'password1', 'password2')
                }),
                ('Personal Info', {
                    'fields': ('first_name', 'last_name', 'email', 'pic')
                }),
                ('Permissions', {
                    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
                }),
                ('Important Dates', {
                    'fields': ('last_login', 'date_joined')
                }),
            )
        return super().get_fieldsets(request, obj)