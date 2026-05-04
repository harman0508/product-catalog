from django.test import TestCase
from catalog.models import Category, Product
from catalog.services.product_service import ProductService


class ServiceTest(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        self.p1 = Product.objects.create(
            title="Laptop", description="A laptop", price="999.99",
            category=self.cat, is_featured=True, priority="high"
        )
        self.p2 = Product.objects.create(
            title="Phone", description="A phone", price="699.99",
            category=self.cat, is_featured=False, priority="low"
        )

    def test_get_products_no_filters(self):
        service = ProductService()
        result = service.get_products(query=None, category=None)
        self.assertEqual(result.count(), 2)

    def test_get_products_search(self):
        service = ProductService()
        result = service.get_products(query="Laptop", category=None)
        self.assertEqual(result.count(), 1)

    def test_get_products_search_no_match(self):
        service = ProductService()
        result = service.get_products(query="Nonexistent", category=None)
        self.assertEqual(result.count(), 0)

    def test_get_products_by_category(self):
        service = ProductService()
        result = service.get_products(query=None, category=str(self.cat.id))
        self.assertEqual(result.count(), 2)

    def test_get_products_invalid_category(self):
        service = ProductService()
        with self.assertRaises(ValueError):
            service.get_products(query=None, category="abc")

    def test_get_featured(self):
        service = ProductService()
        result = service.get_featured()
        self.assertEqual(result.count(), 1)
        self.assertEqual(result.first().title, "Laptop")

    def test_get_by_priority(self):
        service = ProductService()
        result = service.get_by_priority("high")
        self.assertEqual(result.count(), 1)

    def test_get_by_priority_invalid(self):
        service = ProductService()
        with self.assertRaises(ValueError):
            service.get_by_priority("urgent")

    def test_get_products_by_category_id(self):
        service = ProductService()
        result = service.get_products_by_category(self.cat.id)
        self.assertEqual(result.count(), 2)
