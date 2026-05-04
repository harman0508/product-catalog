from django.test import TestCase
from catalog.services.product_service import ProductService


class ServiceTest(TestCase):

    def test_service(self):
        service = ProductService()
        result = service.list_products()
        self.assertIsNotNone(result)