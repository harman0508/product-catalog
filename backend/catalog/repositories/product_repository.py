from catalog.models import Product


class ProductRepository:

    def get_all(self):
        return Product.objects.select_related("category").all()

    def filter(self, query=None, category=None):
        qs = self.get_all()

        if query:
            qs = qs.filter(name__icontains=query.strip())

        if category:
            qs = qs.filter(category_id=category)

        return qs.order_by("id")