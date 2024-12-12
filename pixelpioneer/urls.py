# pixelpioneer/urls.py
from django.urls import path

# from pixelpioneer.views import index
from . import views


urlpatterns = [
    # path('', index),
    path('products', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<int:id>/edit/', views.product_edit, name='product_edit'),
]