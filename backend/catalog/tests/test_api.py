from rest_framework.test import APITestCase
from catalog.models import Category, Product, Inventory


class ProductAPITest(APITestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        self.p1 = Product.objects.create(
            name="Laptop",
            category=self.cat
        )
        Inventory.objects.create(product=self.p1, quantity=10)

    def test_list_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("results", res.data)

    def test_list_returns_inventory(self):
        """Product response should include inventory data."""
        res = self.client.get("/api/products/")
        product = res.data["results"][0]
        self.assertEqual(product["inventory"]["quantity"], 10)

    def test_retrieve_single_product(self):
        res = self.client.get(f"/api/products/{self.p1.id}/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], "Laptop")

    def test_search(self):
        res = self.client.get("/api/products/?q=Laptop")
        self.assertEqual(len(res.data["results"]), 1)

    def test_search_no_results(self):
        res = self.client.get("/api/products/?q=Nonexistent")
        self.assertEqual(len(res.data["results"]), 0)

    def test_filter_by_category(self):
        res = self.client.get(
            f"/api/products/?category={self.cat.id}"
        )
        self.assertEqual(len(res.data["results"]), 1)

    def test_invalid_category(self):
        res = self.client.get("/api/products/?category=abc")
        self.assertEqual(res.status_code, 400)

    def test_write_operations_not_allowed(self):
        """ReadOnlyModelViewSet should reject POST/PUT/DELETE."""
        res = self.client.post(
            "/api/products/",
            {"name": "Test", "category": self.cat.id}
        )
        self.assertIn(res.status_code, [403, 405])

    def test_pagination_structure(self):
        """Response should have pagination fields."""
        res = self.client.get("/api/products/")
        self.assertIn("count", res.data)
        self.assertIn("next", res.data)
        self.assertIn("previous", res.data)
        self.assertIn("results", res.data)


class CategoryAPITest(APITestCase):

    def setUp(self):
        Category.objects.create(name="Electronics")
        Category.objects.create(name="Books")

    def test_list_categories(self):
        res = self.client.get("/api/categories/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 2)

    def test_retrieve_single_category(self):
        cat = Category.objects.first()
        res = self.client.get(f"/api/categories/{cat.id}/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], cat.name)


class EmptyDatasetTest(APITestCase):
    """Edge case: no data in database."""

    def test_empty_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 0)
        self.assertEqual(res.data["results"], [])

    def test_empty_categories(self):
        res = self.client.get("/api/categories/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 0)
