from typing import Optional
from django.db.models import QuerySet
from catalog.models import Product


class ProductRepository:
    """
    Repository layer for database queries related to Product.
    Uses select_related to optimize DB queries.
    """

    def filter(self, query: Optional[str] = None, category: Optional[str] = None) -> QuerySet:
        qs = Product.objects.select_related("category", "inventory").all()

        if query:
            qs = qs.filter(title__icontains=query)

        if category:
            qs = qs.filter(category_id=int(category))

        return qs

    def get_featured(self) -> QuerySet:
        return Product.objects.select_related("category", "inventory").filter(is_featured=True)

    def get_by_priority(self, level: str) -> QuerySet:
        return Product.objects.select_related("category", "inventory").filter(priority=level)

    def get_by_category(self, category_id: int) -> QuerySet:
        return Product.objects.select_related("category", "inventory").filter(category_id=category_id)
