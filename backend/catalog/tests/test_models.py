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

    def test_description_default(self):
        c = Category.objects.create(name="Test")
        self.assertEqual(c.description, "")


class ProductModelTest(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")

    def test_str(self):
        p = Product.objects.create(title="Laptop", category=self.cat)
        self.assertEqual(str(p), "Laptop")

    def test_category_relationship(self):
        p = Product.objects.create(title="Laptop", category=self.cat)
        self.assertEqual(p.category, self.cat)
        self.assertIn(p, self.cat.products.all())

    def test_cascade_delete(self):
        Product.objects.create(title="Laptop", category=self.cat)
        self.cat.delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_is_featured_default(self):
        p = Product.objects.create(title="Laptop", category=self.cat)
        self.assertFalse(p.is_featured)

    def test_priority_default(self):
        p = Product.objects.create(title="Laptop", category=self.cat)
        self.assertEqual(p.priority, "medium")

    def test_priority_choices(self):
        for priority in ["low", "medium", "high", "critical"]:
            p = Product.objects.create(
                title=f"Product-{priority}",
                category=self.cat,
                priority=priority
            )
            self.assertEqual(p.priority, priority)

    def test_price_default(self):
        p = Product.objects.create(title="Laptop", category=self.cat)
        self.assertEqual(p.price, 0)


class InventoryModelTest(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(title="Laptop", category=self.cat)

    def test_str(self):
        inv = Inventory.objects.create(product=self.product, quantity=10)
        self.assertEqual(str(inv), "Laptop - 10")

    def test_one_to_one(self):
        Inventory.objects.create(product=self.product, quantity=10)
        with self.assertRaises(IntegrityError):
            Inventory.objects.create(product=self.product, quantity=20)

    def test_product_inventory_access(self):
        inv = Inventory.objects.create(product=self.product, quantity=15)
        self.assertEqual(self.product.inventory, inv)
        self.assertEqual(self.product.inventory.quantity, 15)
