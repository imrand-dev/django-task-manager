from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

from account.managers import CustomUserManager

from common.base_model import BaseModelWithUID

def full_name(instance):
    if instance.first_name and instance.last_name:
        return f"{instance.first_name} {instance.last_name}".strip()
    return instance.email


class User(AbstractBaseUser, PermissionsMixin, BaseModelWithUID):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = AutoSlugField(
        populate_from=full_name,
        editable=False,
        unique=True,
    )
    email = models.EmailField(unique=True, db_index=True)
    avatar = models.ImageField(
        verbose_name="Profile Picture",
        upload_to="avatar/",
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    
    username = None
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-created_at"]