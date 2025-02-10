from django.shortcuts import render
# CreateView используется для создания нового объекта
from django.views.generic import CreateView

from .models import Article


# Create your views here.

# Создать представление для создания объекта
class ArticleCreateView(CreateView):
    # Указать модель, с которой будет работать представление
    model = Article
    # Определить поля, которые будут отображаться в форме при создании объекта
    fields = ['title', 'content', 'image',]
    # Указать шаблон, который будет отображать форму создания объекта
    template_name = 'article/article_form.html'
    # Определить маршрут, куда пользователь будет перенаправлен после успешного создания объекта
    success_url = '#'

