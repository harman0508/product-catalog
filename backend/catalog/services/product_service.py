from catalog.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.repo = ProductRepository()

    def list_products(self, query=None, category=None):
        return self.repo.filter(query, category)