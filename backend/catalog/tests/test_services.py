from django.test import TestCase
from catalog.models import Category, Product
from catalog.services.product_service import ProductService


class ServiceTest(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        Product.objects.create(name="Laptop", category=self.cat)

    def test_get_products_no_filters(self):
        service = ProductService()
        result = service.get_products(query=None, category=None)
        self.assertEqual(result.count(), 1)

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
        self.assertEqual(result.count(), 1)

    def test_get_products_invalid_category(self):
        service = ProductService()
        with self.assertRaises(ValueError):
            service.get_products(query=None, category="abc")
