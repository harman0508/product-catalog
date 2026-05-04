from django.core.management.base import BaseCommand
from catalog.models import Category, Product, Inventory


class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        cat, _ = Category.objects.get_or_create(name="Electronics")

        p1, _ = Product.objects.get_or_create(name="Laptop", category=cat)
        p2, _ = Product.objects.get_or_create(name="Phone", category=cat)

        Inventory.objects.update_or_create(
            product=p1, defaults={"quantity": 10}
        )

        Inventory.objects.update_or_create(
            product=p2, defaults={"quantity": 20}
        )

        self.stdout.write(self.style.SUCCESS("Seed data created"))