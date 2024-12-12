# pixelpioneer/serializers.py
from rest_framework import serializers
from .models import ProductCard

class ProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCard
        fields = ['id', 'product_name', 'description', 'price', 'image_url', 'category', 'stock', 'created_at', 'updated_at']

    def validate_product_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Product name must be at least 5 characters long")
        return value.strip()

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value
