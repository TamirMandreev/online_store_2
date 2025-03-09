from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

# ModelForm - специальный класс в Django, предназначенный для автоматического создания форм на основе моделей базы данных
class ProductForm(forms.ModelForm):
    # Создать список слов, которые нельзя использовать в названиях и описаниях продуктов
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',]

    # Указать метаданные формы
    class Meta:
        # Указать модель, на которой будет основана форма
        model = Product
        # Определить, какие поля следует исключить из формы
        exclude = ['created_at', 'updated_at']

    # Конструктор формы
    def __init__(self, *args, **kwargs):
        # Вызвать конструктор родительского класса ModelForm
        super(ProductForm, self).__init__(*args, **kwargs)
        # Настроить виджеты формы
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите наименование продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберете изображение'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберете категорию'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену'})

    # Определить метод для валидации и очистки данных, введенных пользователем в поле name
    def clean_name(self):
        # Получить значение поля name
        name = self.cleaned_data['name']
        # Реализовать проверку на запрещенные слова
        for word in self.forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Слово "{word}" нельзя использовать в наименовании продукта')
        # Возвратить наименование продукта
        return name

    # Определить метод для валидации и очистки данных, введенных пользователем в поле description
    def clean_description(self):
        # Получить значение поля name
        description = self.cleaned_data.get('description')
        # Если поле description True
        if description:
            # Реализовать проверку на запрещенные слова
            for word in self.forbidden_words:
                if word in description.lower():
                    raise ValidationError(f'Слово "{word}" нельзя использовать в описании продукта')
        # Возвратить описание продукта
        return description

     # Определить метод для валидации и очистки данных, введенных пользователем в поле price
    def clean_price(self):
        # Получить значение поля price
        price = self.cleaned_data['price']
        # Проверить цену на отрицательное значение
        if price < 0:
            raise ValidationError(f'Цена не может быть отрицательной')
        # Возвратить цену
        return price

# Форма для группы "Модератор продуктов"
class ProductModeratorForm(forms.ModelForm):
    # Указать метаданные формы
    class Meta:
        # Указать модель, на которой будет основана форма
        model = Product
        # Определить поля, которые следует включить в форму
        fields = ['is_published']