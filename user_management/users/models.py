from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    user_email = models.EmailField(max_length=254, verbose_name='Почта')
    phone_num = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Номер телефона')

    def __str__(self):
        return self.first_name
