from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    pic = models.ImageField(_("Profile Picture"), upload_to="images/profile_pics", height_field=None, width_field=None, max_length=None)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change the related name to avoid clash
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change the related name to avoid clash
        blank=True,
    )