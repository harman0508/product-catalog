from django.core.management.base import BaseCommand
from catalog.models import Category, Product, Inventory


class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        electronics, _ = Category.objects.get_or_create(name="Electronics")
        books, _ = Category.objects.get_or_create(name="Books")

        products_data = [
            {"name": "Laptop", "category": electronics, "featured": True, "priority": "high"},
            {"name": "Phone", "category": electronics, "featured": True, "priority": "high"},
            {"name": "Tablet", "category": electronics, "featured": False, "priority": "medium"},
            {"name": "Headphones", "category": electronics, "featured": False, "priority": "low"},
            {"name": "Python Cookbook", "category": books, "featured": True, "priority": "medium"},
            {"name": "Django Guide", "category": books, "featured": False, "priority": "low"},
        ]

        quantities = [10, 20, 15, 50, 30, 25]

        for data, qty in zip(products_data, quantities):
            product, _ = Product.objects.update_or_create(
                name=data["name"],
                defaults={
                    "category": data["category"],
                    "featured": data["featured"],
                    "priority": data["priority"],
                }
            )
            Inventory.objects.update_or_create(
                product=product,
                defaults={"quantity": qty}
            )

        self.stdout.write(self.style.SUCCESS("Seed data created"))
