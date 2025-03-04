from django.db import models
# Испортировать класс AbstractUser. Он предоставляет базовую функциональность для управления пользователями
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Создать модель пользователя
class User(AbstractUser):
    # Удалить поле username
    username = None
    # Использовать email как уникальный идентификатор
    email = models.EmailField(unique=True, verbose_name="Email",)
    # Добавить поле для указания номера телефона
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True, null=True, help_text="Введите номер телефона")
    # Добавить поле для загрузки аватара (изображения)
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name='Аватар', null=True, blank=True, help_text='Загрузите свой аватар')
    # Добавить поле для указания страны
    country = models.CharField(max_length=255, verbose_name="Страна", null=True, blank=True, help_text='Введите страну')

    # Определить поле email как поле для авторизации
    USERNAME_FIELD = ("email")
    REQUIRED_FIELDS = []

    # Добавить дополнительную информацию о самой модели User
    class Meta:
        # Человеко-понятное название модели в единственном числе
        verbose_name = 'Пользователь'
        # Человеко-понятное название модели в множественном числе
        verbose_name_plural = 'Пользователи'

    # Переопределить метод __str__
    def __str__(self):
        return self.email