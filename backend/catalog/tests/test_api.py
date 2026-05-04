from django.test import TestCase
from rest_framework.test import APIClient


class ProductAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_products_list(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)

    def test_invalid_category(self):
        response = self.client.get("/api/products/?category=999")
        self.assertEqual(response.status_code, 200)