from django.core.management.base import BaseCommand
from catalog.models import Category, Product, Inventory


class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name="Electronics")

        p1, _ = Product.objects.get_or_create(name="Laptop", category=category)
        Inventory.objects.get_or_create(product=p1, quantity=10)

        p2, _ = Product.objects.get_or_create(name="Phone", category=category)
        Inventory.objects.get_or_create(product=p2, quantity=25)

        self.stdout.write(self.style.SUCCESS("Seed data created"))