from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.models.mixins import AutoTimestampMixin


class UserManager(BaseUserManager):
    """Менеджер модели пользователя"""

    def create_user(self, email, password=None, **extra_fields):
        """Создание пользователя"""
        if not email:
            raise ValueError('Email обязателен')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создание суперпользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, AutoTimestampMixin):
    """Модель пользователя"""

    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=False, blank=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, blank=True, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, blank=True, verbose_name='Суперпользователь')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Последний вход')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email