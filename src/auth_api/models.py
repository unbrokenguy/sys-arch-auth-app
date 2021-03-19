from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        super().create_superuser(username=email, email=email, password=password)


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


