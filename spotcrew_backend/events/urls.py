from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from events.api.views import EventListView, EventDetailView

urlpatterns = [
    url(r'^api/events/$', EventListView.as_view(), name='list_events'),
    url(r'^api/events/(?P<pk>[0-9]+)$', EventDetailView.as_view(), name='detail_event'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
