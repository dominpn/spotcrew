from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from venues.api.views import VenueDetailView, VenueListView, VenueEventsListView

urlpatterns = [
    url(r'^api/venues/$', VenueListView.as_view(), name='list_venues'),
    url(r'^api/venues/(?P<pk>[0-9]+)$', VenueDetailView.as_view(), name='detail_venue'),
    url(r'^api/venues/(?P<pk>[0-9]+)/events/$', VenueEventsListView.as_view(), name='list_venue_events')
]

urlpatterns = format_suffix_patterns(urlpatterns)
