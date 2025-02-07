from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Импортируем необходимые классы из django.views.generic
# ListView упрощает отображение списка объектов модели
# TemplateView просто отображает HTMl-шаблон
# DetailView отображает подробную информацию об отдельном объекте модели
from django.views.generic import ListView, TemplateView, DetailView

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
    # Указать модель, с которой будет работать контроллер (представление)
    # model = Product
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

#
# # Создать контроллер (представление) для отображения подробной информации о продукте
# class ProductDetailView(DetailView):
#     model = Product

# Создать контроллер (представление) для отображения подробной информации о продукте
def product_detail(request, product_id):
    # Получить объект модели Product по его id
    product = get_object_or_404(Product, pk=product_id)
    # Сформировать контекст для передачи данных в шаблон
    context = {
        'product': product
    }
    # Возвратить клиенту отрендеренную HTML-страницу
    return render(request, 'catalog/product_detail.html', context=context)