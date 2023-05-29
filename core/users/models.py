from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("User name"), max_length=255, unique=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return f"{self.username} || {self.email}"