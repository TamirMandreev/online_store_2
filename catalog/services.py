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

    # Если кэширование выключено
    if not CACHE_ENABLED:
        # Получить список всех продуктов по категории из базы данных
        products_list_by_category = Product.objects.filter(category=category)
        # Возвратить список продуктов
        return products_list_by_category

    # Получить список продуктов по категории из кэша
    products_list_by_category = cache.get('category_name')
    # Если products_list_by_category не пустой
    if products_list_by_category is not None:
        # Возвратить список продуктов по категори
        return products_list_by_category
    # Иначе
    else:
        # Получить список всех продуктов по категории из базы данных
        products_list_by_category = Product.objects.filter(category=category)
        # Возвратить список продуктов по категории
        return products_list_by_category






