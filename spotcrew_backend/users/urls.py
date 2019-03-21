from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from users.api.views import UserDetailView, UserListView

urlpatterns = [
    url(r'^api/users/$', UserListView.as_view(), name='list_users'),
    url(r'^api/events/(?P<pk>[0-9]+)$', UserDetailView.as_view(), name='detail_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
