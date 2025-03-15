from django.urls import path
from . import views
# Функция cache_page используется для кэширования результатов запросов
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('product/<str:category_name>', views.ProductListViewByCategory.as_view(), name='product_list_by_category'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/detail/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]