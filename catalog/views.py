# Класс LoginRequiredMixin обеспечивает защиту представлений.
# Доступ к представлениям доступен только аутентифицированным пользователям
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Импортируем необходимые классы из django.views.generic
# ListView упрощает отображение списка объектов модели
# TemplateView просто отображает HTMl-шаблон
# DetailView отображает подробную информацию об отдельном объекте модели
# CreateView предоставляет простой способ создания новой записи в базе данных через веб-интерфейс
# UpdateView обновляет существующие объекты через веб-интерфейс
# DeleteView удаляет объект. (Отображает страницу подтверждения удаления и обрабатывает запрос на удаление)
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product

# Create your views here.

# Создать контроллер (представление) домашней страницы
class ProductListView(ListView):
    # Указать модель, с которой будет работать контроллер (представление)
    model = Product
    # Указать шаблон, который будет использоваться для отображения списка объектов модели Product
    template_name = 'catalog/home.html'
    # Задать имя переменной, под которой список объектов будет доступен в шаблоне
    context_object_name = 'products'


# Создать контроллер (представление) страницы обратной связи
class ContactsView(LoginRequiredMixin, TemplateView):
    # Указать шаблон отображаемой html-страницы
    template_name = 'catalog/contacts.html'

    # Переопределить метод post
    def post(self, request, *args, **kwargs):
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Выполняем необходимые действия с данными
        print('Данные получены')
        print(f'Name: {name}\nPhone: {phone}\nMessage: {message}')\
        # Отправить пользователю ответ "Данные успешно отправлены"
        return HttpResponse('Данные успешно отправлены')


# Создать контроллер (представление) для отображения подробной информации о продукте
class ProductDetailView(LoginRequiredMixin, DetailView):
    # Указать модель, с которой будет работать контроллер (представление)
    model = Product
    # Указать шаблон, который будет отражать детальную информацию об объекте модели Product
    template_name = 'catalog/product_detail.html'
    # Задать имя переменной, под которой объект будет доступен в шаблоне
    context_object_name = 'product'


# Создать представление для создания объекта модели Product
# Сделать его доступным только для зарегистрированных пользователей
class ProductCreateView(LoginRequiredMixin, CreateView):
    # Указать модель, с которой будет работать представление
    model = Product
    # Интегрировать (подключить) form_class
    form_class = ProductForm
    # Указать шаблон, который будет использоваться для отображения формы
    template_name = 'catalog/product_form.html'
    # Определить URL-адрес, на который будет перенаправлен пользователь после успешной отправки формы
    success_url = reverse_lazy('home')

# Создать представление для редактирования объекта модели Product
# Сделать его доступным только для зарегистрированных пользователей
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    # Указать модель, с которой будет работать представление
    model = Product
    # Подключить form_class
    form_class = ProductForm
    # Указать шаблон, который будет использоваться для отображения формы
    template_name = 'catalog/product_form.html'
    # Определить URL-адрес, на который будет перенаправлен пользователь после успешной отправки формы
    success_url = reverse_lazy('home')

    # Вернуть класс формы, который будет использоваться для обработки ввода данных от пользователя
    def get_form_class(self):
        # Получить пользователя, отправившего запрос
        user = self.request.user
        # Если пользователь - суперюзер
        if user.is_superuser:
            # Вернуть полную форму
            return ProductForm
        # Если пользователь имеет право can_unpublish_product
        elif user.has_perm('catalog.can_unpublish_product'):
            # Вернуть форму для группы "Модератор продуктов"
            return ProductModeratorForm
        # Иначе
        else:
            # Вызвать исключение "Доступ запрещен"
            raise PermissionDenied


# Создать представление для удаления объекта модели Product
# Сделать его доступным только для зарегистрированных пользователей
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    # Указать модель, с которой будет работать представление
    model = Product
    # Указать шаблон, который будет использоваться для отображения формы
    template_name = 'catalog/product_confirm_delete.html'
    # Определить URL-адрес, на который будет перенаправлен пользователь после успешной отправки формы
    success_url = reverse_lazy('home')



