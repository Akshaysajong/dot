from django_filters import FilterSet
from .models import destinstions,icons

class Itemfilter(FilterSet):
    class Meta:
        model=destinstions
        fields = ['id','name']

class categoryfilter(FilterSet):
    class Meta:
        model=icons
        fields = ['id']