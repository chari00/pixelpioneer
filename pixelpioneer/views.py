# pixelpioneer/views.py
# from datetime import datetime


from rest_framework import viewsets
from pixelpioneer.models import ProductCard  # Import from models.py instead
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

    products = ProductCard.objects.all()

    return render(request, 'product_list.html', {'products':products})

def product_detail(request, id):

    product = get_object_or_404(ProductCard, pk=id)

    return render(request, 'product_detail.html', {'product':product})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username='sai')
            post.published_date = timezone.now()
            post.save()

            # messages.success(request, "Post successfully created!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'pixelpioneer/product_edit.html', {'form': form})

def product_edit(request, id):
    product = get_object_or_404(ProductCard, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username='sai')
            post.published_date = timezone.now()
            post.save()

            # messages.success(request, "Post successfully edited!")
            return redirect('product_detail', id=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'pixelpioneer/product_edit.html', {'form': form, 'product':product})
