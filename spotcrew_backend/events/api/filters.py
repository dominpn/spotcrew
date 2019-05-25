from django_filters import rest_framework as filters

from events.models import Event


class EventFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    sport = filters.CharFilter(field_name='sport_id__name')
    start_date__gte = filters.DateFilter(field_name='event_start', lookup_expr='gte')

    class Meta:
        model = Event
        fields = ['name', ]
