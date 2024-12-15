# pixelpioneer/serializers.py
from rest_framework import serializers
from .models import ProductCard

class ProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCard
        fields = ['id', 'product_name', 'description', 'price', 'image', 'category', 'feature', 'is_new', 'stock', 'created_at', 'updated_at']

    def validate_product_name(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Product name must not be empty")
        return value.strip()

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value
