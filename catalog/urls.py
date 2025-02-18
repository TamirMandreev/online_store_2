from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
]