from django import forms
from django.core.exceptions import ValidationError
from pixelpioneer.models import ProductCard

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductCard
        fields = ('product_name', 'description', 'price', 'image_url', 'category', 'stock')
        
        labels = {
            'product_name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'image_url': 'Image URL',
            'category': 'Category',
            'stock': 'Stock'
        }

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        
        if 'forbidden' in product_name.lower():
            raise forms.ValidationError("The product name cannot contain the word 'forbidden'.")

        if len(product_name) < 5:
            raise forms.ValidationError("The product name must be at least 5 characters long.")
        if len(product_name) > 100:
            raise forms.ValidationError("The product name cannot be more than 100 characters long.")

        return product_name.strip()
    
    def clean_description(self):
        description = self.cleaned_data.get('description')

        if len(description) < 10:
            raise forms.ValidationError("The description must be at least 20 characters long.")
        if len(description) > 2000:
            raise forms.ValidationError("The description cannot be more than 2000 characters long.")

        return description.strip()

    
  