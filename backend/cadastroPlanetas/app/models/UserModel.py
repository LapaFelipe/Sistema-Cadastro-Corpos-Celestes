from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


class UserManager(BaseUserManager):
    def _create_user(self, nome, password=None, **extra_fields):
        if not nome:
            raise ValueError("The Email field must be set.")
        user = self.model(username=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name= ('groups'),
        blank=True,
        related_name='app_users'  # Nome relacionado personalizado
    )

    # Defina related_name para user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name= ('user permissions'),
        blank=True,
        related_name='app_users'  # Nome relacionado personalizado
    )