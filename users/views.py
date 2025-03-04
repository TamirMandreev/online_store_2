from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy

# CreateView предоставляет простой способ создания новой записи в базе данных через веб-интерфейс
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


# Create your views here.

# Создать представление для создания объекта модели User
class UserCreateView(CreateView):
    # Указать модель, с которой будет работать представление
    model = User
    # Указать шаблон, который будет использоваться для отображения формы
    template_name = 'users/user_form.html'
    # Интегрировать (подключить) form_class
    form_class = UserRegisterForm
    # Определить URL-адрес, на который будет перенаправлен пользователь после успешной отправки формы
    success_url = reverse_lazy('login')

    # Реализовать отправку приветственного письма пользователю после регистрации
    def form_valid(self, form):
        # Создать объект на основе данных формы регистрации
        user = form.save()
        # Отправить приветственное письмо пользователю
        send_mail(subject='Успешная регистрация',
                  message='Спасибо, что зарегистрировались на нашем сайте',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email],)

        return super().form_valid(form)