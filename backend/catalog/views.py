from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from catalog.models import Product, Category
from catalog.serializers import ProductSerializer, CategorySerializer
from catalog.services.product_service import ProductService


class ProductViewSet(viewsets.ModelViewSet):
    """
    Full CRUD API endpoint for products.

    Supports listing, retrieval, creation, update, deletion,
    search, category filtering, ordering, pagination, and custom actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'priority', 'is_featured']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'price', 'priority']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """GET /api/products/featured/ — Returns all featured products."""
        featured_products = self.get_queryset().filter(is_featured=True)
        page = self.paginate_queryset(featured_products)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by_priority')
    def by_priority(self, request):
        """GET /api/products/by_priority/?level=high — Filter by priority."""
        level = request.GET.get('level')
        if not level:
            return Response(
                {'error': "Query parameter 'level' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        service = ProductService()
        try:
            products = service.get_by_priority(level)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Full CRUD API endpoint for categories.

    Includes nested route for listing products in a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """GET /api/categories/{id}/products/ — Products in this category."""
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
