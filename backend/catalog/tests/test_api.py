from rest_framework.test import APITestCase
from catalog.models import Category, Product, Inventory


class ProductAPITest(APITestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        self.p1 = Product.objects.create(
            name="Laptop", category=self.cat, featured=True, priority="high"
        )
        self.p2 = Product.objects.create(
            name="Phone", category=self.cat, featured=False, priority="low"
        )
        Inventory.objects.create(product=self.p1, quantity=10)

    # --- List / Retrieve ---

    def test_list_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("results", res.data)

    def test_list_returns_inventory(self):
        res = self.client.get("/api/products/")
        product = next(p for p in res.data["results"] if p["name"] == "Laptop")
        self.assertEqual(product["inventory"]["quantity"], 10)

    def test_retrieve_single_product(self):
        res = self.client.get(f"/api/products/{self.p1.id}/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], "Laptop")

    # --- Create ---

    def test_create_product(self):
        res = self.client.post("/api/products/", {
            "name": "Tablet",
            "category": self.cat.id,
            "priority": "medium"
        })
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["name"], "Tablet")

    def test_create_product_invalid_name(self):
        res = self.client.post("/api/products/", {
            "name": "X",
            "category": self.cat.id
        })
        self.assertEqual(res.status_code, 400)

    # --- Update ---

    def test_update_product(self):
        res = self.client.put(f"/api/products/{self.p1.id}/", {
            "name": "Gaming Laptop",
            "category": self.cat.id,
            "priority": "high"
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], "Gaming Laptop")

    # --- Delete ---

    def test_delete_product(self):
        res = self.client.delete(f"/api/products/{self.p2.id}/")
        self.assertEqual(res.status_code, 204)
        self.assertEqual(Product.objects.count(), 1)

    # --- Search / Filter ---

    def test_search(self):
        res = self.client.get("/api/products/?q=Laptop")
        self.assertEqual(len(res.data["results"]), 1)

    def test_search_no_results(self):
        res = self.client.get("/api/products/?q=Nonexistent")
        self.assertEqual(len(res.data["results"]), 0)

    def test_filter_by_category(self):
        res = self.client.get(f"/api/products/?category={self.cat.id}")
        self.assertEqual(len(res.data["results"]), 2)

    def test_invalid_category(self):
        res = self.client.get("/api/products/?category=abc")
        self.assertEqual(res.status_code, 400)

    # --- Custom Actions ---

    def test_featured_products(self):
        res = self.client.get("/api/products/featured/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data["results"]), 1)
        self.assertEqual(res.data["results"][0]["name"], "Laptop")

    def test_by_priority(self):
        res = self.client.get("/api/products/by_priority/?level=high")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data["results"]), 1)
        self.assertEqual(res.data["results"][0]["name"], "Laptop")

    def test_by_priority_missing_level(self):
        res = self.client.get("/api/products/by_priority/")
        self.assertEqual(res.status_code, 400)

    def test_by_priority_invalid_level(self):
        res = self.client.get("/api/products/by_priority/?level=urgent")
        self.assertEqual(res.status_code, 400)

    # --- Pagination ---

    def test_pagination_structure(self):
        res = self.client.get("/api/products/")
        self.assertIn("count", res.data)
        self.assertIn("next", res.data)
        self.assertIn("previous", res.data)
        self.assertIn("results", res.data)

    # --- New fields in response ---

    def test_response_includes_featured_and_priority(self):
        res = self.client.get(f"/api/products/{self.p1.id}/")
        self.assertIn("featured", res.data)
        self.assertIn("priority", res.data)
        self.assertTrue(res.data["featured"])
        self.assertEqual(res.data["priority"], "high")


class CategoryAPITest(APITestCase):

    def setUp(self):
        self.cat = Category.objects.create(name="Electronics")
        Category.objects.create(name="Books")
        Product.objects.create(name="Laptop", category=self.cat, priority="high")

    def test_list_categories(self):
        res = self.client.get("/api/categories/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 2)

    def test_retrieve_single_category(self):
        res = self.client.get(f"/api/categories/{self.cat.id}/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], "Electronics")

    def test_create_category(self):
        res = self.client.post("/api/categories/", {"name": "Clothing"})
        self.assertEqual(res.status_code, 201)

    def test_update_category(self):
        res = self.client.put(
            f"/api/categories/{self.cat.id}/",
            {"name": "Tech"}
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], "Tech")

    def test_delete_category(self):
        cat = Category.objects.create(name="ToDelete")
        res = self.client.delete(f"/api/categories/{cat.id}/")
        self.assertEqual(res.status_code, 204)

    def test_category_products(self):
        """GET /api/categories/{id}/products/ — nested route."""
        res = self.client.get(f"/api/categories/{self.cat.id}/products/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["name"], "Laptop")


class EmptyDatasetTest(APITestCase):

    def test_empty_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 0)

    def test_empty_categories(self):
        res = self.client.get("/api/categories/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 0)

    def test_empty_featured(self):
        res = self.client.get("/api/products/featured/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["count"], 0)
