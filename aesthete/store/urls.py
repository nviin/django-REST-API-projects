"""
URL configuration for aesthete project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store import views
from .views import ProductFilterViewSet, ProductSearchViewSet
from cart.views import CartViewSet

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename = 'category')
router.register(r'products', views.ProductViewSet, basename = 'product')
router.register(r'filter', ProductFilterViewSet, basename='product-filter')
router.register(r'search', ProductSearchViewSet, basename='product-search')
router.register(r'cart', CartViewSet, basename='cart')
urlpatterns = [
    path('', include(router.urls)),
]
