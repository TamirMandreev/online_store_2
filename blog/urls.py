from django.urls import path
from blog import views

urlpatterns = [
    path('blog/create', views.ArticleCreateView.as_view(), name='blog_create'),
]