from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]