from django.shortcuts import render
from store.serializers import ProductSerializer,CategorySerializer
from store.models import Category, Products
from rest_framework import viewsets, filters
from store.filters import ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # filterset_class = CategoryFilter

class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()

class ProductFilterViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    filterset_class = ProductFilter

class ProductSearchViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'hashtags', 'category__name']




