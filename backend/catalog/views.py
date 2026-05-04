from rest_framework import viewsets, status
from rest_framework.response import Response
from catalog.models import Product, Category
from catalog.serializers import ProductSerializer, CategorySerializer
from catalog.services.product_service import ProductService


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for products.

    Supports listing, retrieval, search, category filtering, and pagination.
    Uses service layer for business logic separation.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        service = ProductService()
        query = request.GET.get("q")
        category = request.GET.get("category")

        try:
            products = service.get_products(query, category)
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
