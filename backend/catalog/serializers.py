from rest_framework import serializers
from .models import Product, Category, Inventory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["quantity"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "category", "category_name", "inventory"]

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name too short")
        return value