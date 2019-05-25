from django_filters import rest_framework as filters

from venues.models import Venue


class VenueFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Venue
        fields = ['name', ]
