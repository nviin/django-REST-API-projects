import django_filters

from store.models import Products, Category


class ProductFilter(django_filters.FilterSet):
    class Meta:

        model = Products
        fields = {
            'price': ['exact','lt','gt','lte','gte','range'],
            'hashtags': ['exact', 'contains']
        }



