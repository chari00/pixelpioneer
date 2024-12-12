from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllProducts),
    path('add/', views.addProduct),
    path('get/<int:id>/', views.getProductById, name='get_product_by_id'),
    path('delete/<int:id>/', views.deleteProduct, name='delete_product'),
    path('update/<int:id>/', views.updateProduct, name='update_product'),
]