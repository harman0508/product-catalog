from typing import Optional
from django.db.models import QuerySet
from catalog.models import Product


class ProductRepository:
    """
    Repository layer for database queries related to Product.
    """

    def filter(self, query: Optional[str], category: Optional[str]) -> QuerySet:
        """
        Filters products by search query and category.
        Uses select_related to optimize DB queries.
        """
        qs = Product.objects.select_related("category", "inventory").all()

        if query:
            qs = qs.filter(name__icontains=query)

        if category:
            qs = qs.filter(category_id=int(category))

        return qs