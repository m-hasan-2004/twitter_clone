from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, Group, Permission
from uuid import uuid4
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    objects = UserManager()
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pic = models.ImageField(_("Profile Picture"), upload_to="images/profile_pics", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
    )