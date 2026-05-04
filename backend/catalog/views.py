from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .services.product_service import ProductService


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        query = self.request.GET.get("q")
        category = self.request.GET.get("category")

        service = ProductService()
        return service.list_products(query, category)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer