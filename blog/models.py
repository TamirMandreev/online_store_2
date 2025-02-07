from django.db import models

# Create your models here.

# Создать модель Article
class Article(models.Model):
    # Заголовок статьи
    title = models.CharField(max_length=200, verbose_name='Заголовок', help_text='Введите заголовок статьи')
    # Содержимое статьи
    content = models.TextField(blank=True, null=True, verbose_name='Содержимое', help_text='Введите содержимое статьи')
    # Изображение
    image = models.ImageField(upload_to='blog_image', verbose_name='Изображение', blank=True, null=True, help_text='Загрузите изображение')
    # Дата создания
    create_at = models.DateTimeField(auto_now_add=True)
    # Опубликована статья или нет
    is_published = models.BooleanField(default=True)
    # Количество просмотров
    views_count = models.IntegerField(default=0)

    # Переопределить метод __str__
    def __str__(self):
        return self.title

    # Добавить дополнительную информацию о самой модели Article
    class Meta:
        # Человеко-понятное название модели в единственном числе
        verbose_name = 'статья'
        # Человеко-понятное название модели в множественном числе
        verbose_name_plural = 'статьи'
        # Имя таблицы в базе данных, которое будет соответствовать данной модели
        db_table = 'Статьи'