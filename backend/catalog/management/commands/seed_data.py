from django.core.management.base import BaseCommand
from catalog.models import Category, Product, Inventory


class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        electronics, _ = Category.objects.get_or_create(
            name="Electronics",
            defaults={"description": "Latest gadgets and electronic devices"}
        )
        books, _ = Category.objects.get_or_create(
            name="Books",
            defaults={"description": "Books, magazines, and reading materials"}
        )

        products_data = [
            {"title": "Laptop", "description": "High-performance laptop", "category": electronics, "is_featured": True, "priority": "high", "price": "999.99"},
            {"title": "Phone", "description": "Latest smartphone", "category": electronics, "is_featured": True, "priority": "high", "price": "699.99"},
            {"title": "Tablet", "description": "Portable tablet", "category": electronics, "is_featured": False, "priority": "medium", "price": "449.99"},
            {"title": "Headphones", "description": "Wireless headphones", "category": electronics, "is_featured": False, "priority": "low", "price": "149.99"},
            {"title": "Python Cookbook", "description": "Comprehensive Python guide", "category": books, "is_featured": True, "priority": "medium", "price": "44.99"},
            {"title": "Django Guide", "description": "Django web framework guide", "category": books, "is_featured": False, "priority": "low", "price": "39.99"},
        ]

        quantities = [10, 20, 15, 50, 30, 25]

        for data, qty in zip(products_data, quantities):
            product, _ = Product.objects.update_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "category": data["category"],
                    "is_featured": data["is_featured"],
                    "priority": data["priority"],
                    "price": data["price"],
                }
            )
            Inventory.objects.update_or_create(
                product=product,
                defaults={"quantity": qty}
            )

        self.stdout.write(self.style.SUCCESS("Seed data created"))
