from django.shortcuts import render
# CreateView используется для создания нового объекта
# ListView упрощает отображение списка объектов модели
from django.views.generic import CreateView, ListView

from .models import Article


# Create your views here.

# Создать представление для создания объекта модели Article
class ArticleCreateView(CreateView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Определить поля, которые будут отображаться в форме при создании объекта
    fields = ['title', 'content', 'image',]
    # Указать шаблон, который будет отображать форму создания объекта
    template_name = 'article/article_form.html'
    # Определить маршрут, куда пользователь будет перенаправлен после успешного создания объекта
    success_url = '#'

# Создать представление для отображения списка объектов модели Article
class ArticleListView(ListView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Указать шаблон, который будет использоваться для отображения списка объектов модели Article
    template_name = 'article/article_list.html'
    # Задать имя переменной, под которой список объектов будет доступен в шаблоне
    context_object_name = 'articles'

