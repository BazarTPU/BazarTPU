from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    telegram = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telegram')
    dormitory = models.CharField(max_length=100, blank=True, null=True, verbose_name='Общежитие')
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True,
        verbose_name='Фото профиля',
        default='profile_photos/noLogoItem900.png'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

