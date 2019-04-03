from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from tokens.users.views import activate

urlpatterns = [
    url(r'^api/token/activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
