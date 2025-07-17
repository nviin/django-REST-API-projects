from rest_framework import serializers
from cart.models import Usercart, Cartitems

from store.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = Cartitems
        fields = ['id', 'cart', 'product']

class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many = True)
    class Meta:
        model = Usercart
        fields = ['cart_id', 'items']


