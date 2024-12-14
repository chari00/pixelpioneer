from django.contrib import admin

from pixelpioneer.models import ProductCard

class PostProductCard(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category', 'feature', 'is_new', 'stock')

# Register your models here.
admin.site.register(ProductCard, PostProductCard)