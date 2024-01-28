from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    country = models.CharField(max_length=150, verbose_name='страна')
    phone = models.CharField(max_length=10, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
