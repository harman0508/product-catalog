from typing import Optional
from django.db.models import QuerySet
from catalog.models import Product
from catalog.repositories.product_repository import ProductRepository


class ProductService:
    """
    Service layer for product-related business logic.

    Handles filtering, validation, and orchestration between
    views and repository layer.
    """

    def __init__(self, repo: Optional[ProductRepository] = None):
        self.repo = repo or ProductRepository()

    def get_products(self, query: Optional[str], category: Optional[str]) -> QuerySet:
        """
        Returns filtered products with validation.

        Args:
            query: search string
            category: category id (string from request)

        Raises:
            ValueError: if category is invalid
        """
        if category:
            if not category.isdigit():
                raise ValueError("Invalid category id")

        return self.repo.filter(query=query, category=category)