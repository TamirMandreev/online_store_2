# Класс LogoutView обеспечивает безопасный выход текущего пользователя из системы,
# очистку сессии и перенаправление на указанный URL после
# успешного завершения операции.
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


