from django.urls import path
from blog import views

urlpatterns = [
    path('blog/create/', views.ArticleCreateView.as_view(), name='blog_create'),
    path('blog/', views.ArticleListView.as_view(), name='blog_list'),
    path('blog/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='blog_detail'),
]