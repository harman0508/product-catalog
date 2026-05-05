from rest_framework import serializers
from .models import Product, Category, Inventory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'category', 'category_name',
            'price', 'priority', 'is_featured', 'image_url',
            'inventory', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Title too short")
        return value


class ProductListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views."""
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'category', 'category_name',
            'price', 'priority', 'is_featured', 'image_url'
        ]
