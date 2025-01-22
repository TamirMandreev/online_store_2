from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


# Create your views here.

# Создать контроллер (представление) домашней страницы
def home(request):
    # Получить все объекты модели Product
    products = Product.objects.all()
    # Сформировать контекст для передачи переменных в шаблон
    context = {
       'products': products
    }
    # Возвратить клиенту отрендеренную HTML-страницу
    return render(request, 'catalog/home.html', context=context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Спасибо, {name}! Сообщение получено')
    return render(request, 'catalog/contacts.html')
