# pixelpioneer/urls.py
from django.urls import path

# from pixelpioneer.views import index
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.product_list, name='product_list'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/<int:id>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:id>/delete/', views.product_delete, name='product_delete'),

]