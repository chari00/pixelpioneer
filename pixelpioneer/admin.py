from django.contrib import admin

from pixelpioneer.models import ProductCard

class PostProductCard(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category', 'stock')

# Register your models here.
admin.site.register(ProductCard, PostProductCard)