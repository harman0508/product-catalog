from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from catalog.models import Product, Category
from catalog.serializers import ProductSerializer, CategorySerializer
from catalog.services.product_service import ProductService


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for products.

    Supports CRUD, filtering, search, and pagination.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        """
        List products with optional filtering.
        """
        service = ProductService()

        query = request.GET.get("q")
        category = request.GET.get("category")

        try:
            products = service.get_products(query, category)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]