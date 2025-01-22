from django.contrib import admin

# Импортировать модели Product и Category
from .models import Product, Category

# Register your models here.

# Зарегистрировать модель Product в панели администратора
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Список отображаемых полей
    list_display = ('id', 'name', 'price', 'category',)
    # Фильтрация по полям
    list_filter = ('category',)
    # Список полей, по которым будет производиться поиск введенной фразы
    search_fields = ('name', 'description',)


# Зарегистрировать модель Category в панели администратора
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Список отображаемых полей
    list_display = ('id', 'name',)


