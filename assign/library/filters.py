
import django_filters
from .models import *

# filtering publishers
class PublisherFilter(django_filters.FilterSet):
    class Meta:
        model = Publisher
        fields = ['name',]

# we proceed to view.py






