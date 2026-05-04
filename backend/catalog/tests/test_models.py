from django.test import TestCase
from django.db import IntegrityError
from catalog.models import Category, Product, Inventory


class CategoryModelTest(TestCase):

    def test_str(self):
        c = Category.objects.create(name="Electronics")
        self.assertEqual(str(c), "Electronics")

    def test_name_indexed(self):
        field = Category._meta.get_field("name")
        self.assertTrue(field.db_index)


class ProductModelTest(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")

    def test_str(self):
        p = Product.objects.create(name="Laptop", category=self.cat)
        self.assertEqual(str(p), "Laptop")

    def test_category_relationship(self):
        p = Product.objects.create(name="Laptop", category=self.cat)
        self.assertEqual(p.category, self.cat)
        self.assertIn(p, self.cat.products.all())

    def test_cascade_delete(self):
        """Deleting a category should delete its products."""
        Product.objects.create(name="Laptop", category=self.cat)
        self.cat.delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_featured_default(self):
        p = Product.objects.create(name="Laptop", category=self.cat)
        self.assertFalse(p.featured)

    def test_priority_default(self):
        p = Product.objects.create(name="Laptop", category=self.cat)
        self.assertEqual(p.priority, "medium")

    def test_priority_choices(self):
        for priority in ["high", "medium", "low"]:
            p = Product.objects.create(
                name=f"Product-{priority}",
                category=self.cat,
                priority=priority
            )
            self.assertEqual(p.priority, priority)


class InventoryModelTest(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(name="Laptop", category=self.cat)

    def test_str(self):
        inv = Inventory.objects.create(product=self.product, quantity=10)
        self.assertEqual(str(inv), "Laptop - 10")

    def test_one_to_one(self):
        """Only one inventory per product."""
        Inventory.objects.create(product=self.product, quantity=10)
        with self.assertRaises(IntegrityError):
            Inventory.objects.create(product=self.product, quantity=20)

    def test_product_inventory_access(self):
        """Product can access inventory via related_name."""
        inv = Inventory.objects.create(product=self.product, quantity=15)
        self.assertEqual(self.product.inventory, inv)
        self.assertEqual(self.product.inventory.quantity, 15)
