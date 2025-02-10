from django.shortcuts import render
# CreateView используется для создания нового объекта
# ListView упрощает отображение списка объектов модели
# DetailView отображает подробную информацию об объекте модели
# UpdateView используется для обновления существующего объекта
# DeleteView используется для удаления существующего объекта
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

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

# Создать представление для отображения списка объектов модели Article (домашняя страница блога)
class ArticleListView(ListView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Указать шаблон, который будет использоваться для отображения списка объектов модели Article
    template_name = 'article/home.html'
    # Задать имя переменной, под которой список объектов будет доступен в шаблоне
    context_object_name = 'articles'


# Создать представление для отображения подробной информации об объекте модели Article
class ArticleDetailView(DetailView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Указать шаблон, который будет использоваться для отображения подробной информации об объекте модели Article
    template_name = 'article/article_detail.html'
    # Задать имя переменной, под которой объект будет доступен в шаблоне
    context_object_name = 'article'

# Создать представление для изменения объекта модели Article
class ArticleUpdateView(UpdateView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Указать поля, которые будут отображаться в форме при изменении объекта
    fields = ['title', 'content', 'image',]
    # Указать шаблон, который будет отображать форму изменения объекта
    template_name = 'article/article_form.html'
    # Указать маршрут, куда пользователь будет перенаправлен после успешного изменения объекта
    success_url = '#'

# Создать представление для удаления объекта модели Article
class ArticleDeleteView(DeleteView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Указать шаблон, который будет отображать страницу удаления объекта
    template_name = 'article/article_confirm_delete.html'
    # Задать имя переменной, под которой объект будет доступен в шаблоне
    context_object_name = 'article'
    # Указать маршрут, куда пользователь будет перенаправлен после успешного удаления объекта
    success_url = 'article/home.html'
