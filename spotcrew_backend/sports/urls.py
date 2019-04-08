from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from sports.api.views import SportListView, SportDetailView

urlpatterns = [
    url(r'^api/sports/$', SportListView.as_view(), name='list_sports'),
    url(r'^api/sports/(?P<pk>[0-9]+)$', SportDetailView.as_view(), name='detail_sport'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
