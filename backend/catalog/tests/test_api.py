from rest_framework.test import APITestCase
from catalog.models import Category, Product


class ProductAPITest(APITestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        Product.objects.create(name="Laptop", category=self.cat)

    def test_list_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("results", res.data)

    def test_search(self):
        res = self.client.get("/api/products/?q=Laptop")
        self.assertEqual(len(res.data["results"]), 1)

    def test_invalid_category(self):
        res = self.client.get("/api/products/?category=abc")
        self.assertEqual(res.status_code, 400)