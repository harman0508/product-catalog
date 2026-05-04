from typing import Optional
from django.db.models import QuerySet
from catalog.models import Product
from catalog.repositories.product_repository import ProductRepository


VALID_PRIORITIES = {"low", "medium", "high", "critical"}


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

        Raises:
            ValueError: if category is invalid
        """
        if category:
            if not category.isdigit():
                raise ValueError("Invalid category id")

        return self.repo.filter(query=query, category=category)

    def get_featured(self) -> QuerySet:
        """Returns all featured products."""
        return self.repo.get_featured()

    def get_by_priority(self, level: str) -> QuerySet:
        """
        Returns products filtered by priority level.

        Raises:
            ValueError: if priority level is invalid
        """
        if level not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority level. Must be one of: {', '.join(sorted(VALID_PRIORITIES))}")

        return self.repo.get_by_priority(level)

    def get_products_by_category(self, category_id: int) -> QuerySet:
        """Returns all products in a given category."""
        return self.repo.get_by_category(category_id)
