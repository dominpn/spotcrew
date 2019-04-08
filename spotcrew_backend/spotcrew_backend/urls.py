from django.urls import include
from django.conf.urls import url

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^api/docs/', include_docs_urls(title='Spotcrew API')),
    url(r'^', include('events.urls')),
    url(r'^', include('sports.urls')),
    url(r'^', include('tokens.jwt.urls')),
    url(r'^', include('tokens.users.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('venues.urls')),
]
