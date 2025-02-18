from django import forms

from catalog.models import Product

# ModelForm - специальный класс в Django, предназначенный для автоматического создания форм на основе моделей базы данных
class ProductForm(forms.ModelForm):
    class Meta:
        # Указать модель, на которой будет основана форма
        model = Product
        # Определить, какие поля следует исключить из формы
        exclude = ['created_at', 'updated_at']