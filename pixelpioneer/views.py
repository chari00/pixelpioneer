# pixelpioneer/views.py
# from datetime import datetime


from rest_framework import viewsets
from pixelpioneer.models import ProductCard  
from pixelpioneer.serializers import ProductCardSerializer

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import ProductForm

class ProductCardViewSet(viewsets.ModelViewSet):
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer

   
def index(request):
    return render(request, 'index.html')


def product_list(request):
    category = request.GET.get('category', '')
    if category:
        products = ProductCard.objects.filter(category__icontains=category)
    else:
        products = ProductCard.objects.all()

    return render(request, 'pixelpioneer/product_list.html', {'products':products})

def product_detail(request, id):

    product = get_object_or_404(ProductCard, pk=id)

    return render(request, 'pixelpioneer/product_detail.html', {'product':product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'pixelpioneer/product_edit.html', {'form': form})


def product_edit(request, id):
    product = get_object_or_404(ProductCard, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()

            return redirect('product_detail', id=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'pixelpioneer/product_edit.html', {'form': form, 'product':product})

def product_delete(request, id):
    product = get_object_or_404(ProductCard, pk=id)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    
    return render(request, 'pixelpioneer/product_confirm_delete.html', {'product': product})
