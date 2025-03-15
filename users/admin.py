from django.contrib import admin
# Импортировать модель User
from users.models import User
# Register your models here.

# Зарегистрировать модель User в панели администратора
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Список отображаемых полей
    list_display = ('id', 'email')
