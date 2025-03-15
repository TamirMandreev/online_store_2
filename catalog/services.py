from django.shortcuts import get_object_or_404

from config.settings import CACHE_ENABLED
from .models import Product, Category
# cache - интерфейс для работы с различными системами кэширования
from django.core.cache import cache


def get_products_from_cache(category_name):
    '''
    Возвращает список всех продуктов по указанной категории
    :param category_name:
    :return:
    '''
    # Получить категорию
    category = get_object_or_404(Category, name=category_name)
    # Получить список всех продуктов из категории
    products_list_by_category = Product.objects.filter(category=category)
    # Возвратить список продуктов
    return products_list_by_category
