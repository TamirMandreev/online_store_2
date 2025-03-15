# Класс BaseCommand используется для создания собственных команд управления
from django.core.management import BaseCommand
from users.models import User

# Создать подкласс BaseCommand
class Command(BaseCommand):
    # Основной метод, который выполняется при запуске команды
    def handle(self, *args, **options):
        # Создать пользователя
        user = User.objects.create(email='tamirmandreev@mail.ru')
        # Установить для пользователя пароль
        user.set_password('12345678')
        # Активировать аккаунт пользователя
        user.is_active = True
        # Сделать пользователя членом персонала сайта
        user.is_staff = True
        # Сделать пользователя суперпользователем
        user.is_superuser = True
        # Сохранить пользователя
        user.save()

