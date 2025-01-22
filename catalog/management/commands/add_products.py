# Импортировать базовый класс BaseCommand для создания пользовательских команд
from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Product, Category

# Создать команду, которая будет добавлять тестовые продукты в базу данных
class Command(BaseCommand):
    # Создать строку помощи при вызове команды с параметром --help
    help = 'Add products'

    # Создать метод, который выполняет основную логику команды
    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('Загрузка данных ...')
        # Функция call_command позволяет вызывать команды управления Django программным способом
        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные загружены'))


