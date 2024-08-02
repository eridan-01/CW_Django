from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        **NULLABLE,
        help_text="Загрузите фото"
    )
    phone_number = PhoneNumberField(
        **NULLABLE,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона"
    )
    country = models.CharField(
        **NULLABLE,
        max_length=50,
        verbose_name="Город",
        help_text="Введите город"
    )

    token = models.CharField(
        **NULLABLE,
        max_length=100,
        verbose_name="Токен",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        permissions = [
            ('block_user', 'Может блокировать пользователя'),
        ]

    def __str__(self):
        return self.email
