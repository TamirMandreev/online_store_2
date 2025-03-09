from users.models import User

# Импортировать класс UserCreationForm
# Этот класс предоставляет готовую форму для создания новых пользователей
# Он включает в себя стандартные поля для ввода паролей и проверки их совпадения.
from django.contrib.auth.forms import UserCreationForm


# Создать кастомный класс для переопределения базовой формы регистрации
class UserRegisterForm(UserCreationForm):
    class Meta:
        # Указать модель, на основе которой будет создана форма
        model = User
        # Определить поля, которые будут включены в форму регистрации
        fields = ['email', 'password1', 'password2']