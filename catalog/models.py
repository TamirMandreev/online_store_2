from django.db import models

# Create your models here.

# Создать модель Product
class Product(models.Model):
    # Наименование товара
    name = models.CharField(max_length=150, verbose_name='Наименование')
    # Описание товара
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание товара')
    # Фотография товара
    image = models.ImageField(verbose_name='Фотография')
    # Категория товара
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    # Цена товара
    price = models.DecimalField(max_digits=12, decimal_places=2)
    # Дата и время создания
    created_at = models.DateTimeField(auto_now_add=True)
    # Дата и время последнего изменения и
    updated_at = models.DateTimeField(auto_now=True)

    # Добавить дополнительную информацию о самой модели Product
    class Meta:
        # Человеко-понятное название модели в единственном числе
        verbose_name = 'товар'
        # Человеко-понятное название модели в множественном числе
        verbose_name_plural = 'товары'
        # Сортировку производить по полю name
        ordering = ['name']
        # Имя таблицы в базе данных, которое будет соответствовать данной модели
        db_table = 'Товары'

# Создать модель Category
class Category(models.Model):
    # Наименование категории
    name = models.CharField(max_length=150, verbose_name='Наименование')
    # Описание категории
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание категории')

    # Добавить дополнительную информацию о самой модели Category
    class Meta:
        # Человеко-понятное название модели в единственном числе
        verbose_name = 'категория'
        # Человеко-понятное название модели в множественном числе
        verbose_name_plural = 'категории'
        # Имя таблицы в базе данных, которое будет соответствовать данной модели
        db_table = 'Категории'
