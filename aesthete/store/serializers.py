from rest_framework import serializers
from store.models import Category, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['title', 'price', 'category', 'product_images', 'hashtags']