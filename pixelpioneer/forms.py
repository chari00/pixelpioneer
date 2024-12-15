from django import forms
from django.core.exceptions import ValidationError
from pixelpioneer.models import ProductCard

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductCard
        fields = ('product_name', 'description', 'price', 'image', 'category', 'feature', 'is_new' 'stock')
        
        labels = {
            'product_name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'image': 'Image',
            'feature': 'Featured',
            'is_new': 'New Product',
            'category': 'Category',
            'stock': 'Stock'
        }

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        
        if 'forbidden' in product_name.lower():
            raise forms.ValidationError("The product name cannot contain the word 'forbidden'.")

        if len(product_name) < 1 :
            raise forms.ValidationError("The product name must not be empty.")
        if len(product_name) > 100:
            raise forms.ValidationError("The product name cannot be more than 100 characters long.")

        return product_name.strip()
    
    def clean_description(self):
        description = self.cleaned_data.get('description')

        if len(description) < 10:
            raise forms.ValidationError("The description must be at least 10 characters long.")
        if len(description) > 1500:
            raise forms.ValidationError("The description cannot be more than 1500 characters long.")

        return description.strip()

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        if price > 999999.99:  
            raise forms.ValidationError("Price cannot exceed 999,999.99")

        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')

        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        if stock > 9999:  
            raise forms.ValidationError("Stock cannot exceed 9,999 units.")

        return stock

  