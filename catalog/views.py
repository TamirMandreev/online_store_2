from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.

# Создать контроллер (представление) домашней страницы
def home(request):
    # Получить все объекты модели Product
    products = Product.objects.all()
    # Сформировать контекст для передачи данных в шаблон
    context = {
       'products': products
    }
    # Возвратить клиенту отрендеренную HTML-страницу
    return render(request, 'catalog/home.html', context=context)

# Создать контроллер (представление) страницы обратной связи
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Спасибо, {name}! Сообщение получено')
    return render(request, 'catalog/contacts.html')

def product_detail(request, product_id):
    # Получить объект модели Product по его id
    product = get_object_or_404(Product, pk=product_id)
    # Сформировать контекст для передачи данных в шаблон
    context = {
        'product': product
    }
    # Возвратить клиенту отрендеренную HTML-страницу
    return render(request, 'catalog/product_detail.html', context=context)