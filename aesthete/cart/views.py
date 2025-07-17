from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from cart.models import Usercart
from cart.serializers import CartSerializer

class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):

    queryset = Usercart.objects.all()
    serializer_class = CartSerializer




