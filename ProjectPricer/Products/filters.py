from django_filters import CharFilter,OrderingFilter
import django_filters
from .models import *
class Product_filter(django_filters.FilterSet):
    name = CharFilter(lookup_expr='icontains')
    name_or = OrderingFilter(field_name='name')
    class Meta:
        model=Product
        fields = ['name','name_or']
