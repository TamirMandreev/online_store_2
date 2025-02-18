from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Импортируем необходимые классы из django.views.generic
# ListView упрощает отображение списка объектов модели
# TemplateView просто отображает HTMl-шаблон
# DetailView отображает подробную информацию об отдельном объекте модели
# CreateView предоставляет простой способ создания новой записи в базе данных через веб-интерфейс
from django.views.generic import ListView, TemplateView, DetailView, CreateView

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
class ContactsView(TemplateView):
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
class ProductDetailView(DetailView):
    # Указать модель, с которой будет работать контроллер (представление)
    model = Product
    # Указать шаблон, который будет отражать детальную информацию об объекте модели Product
    template_name = 'catalog/product_detail.html'
    # Задать имя переменной, под которой объект будет доступен в шаблоне
    context_object_name = 'product'


# Создать представление для создания объекта модели Product
class ProductCreateView(CreateView):
    # Указать модель, с которой будет работать представление
    model = Product
    # Указать список полей, которые будут доступны для редактирования в форме
    fields = '__all__'
    # Определить список полей, которые будут недоступны для редактирования в форме
    exclude = ['created_at', 'updated_at']
    # Указать шаблон, который будет использоваться для отображения формы
    template_name = 'catalog/product_form.html'
    # Определить URL-адрес, на который будет перенаправлен пользователь после успешной отправки формы
    success_url = reverse_lazy('home')
