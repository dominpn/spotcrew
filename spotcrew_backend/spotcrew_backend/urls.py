from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^', include('events.urls')),
    url(r'^', include('tokens.jwt.urls')),
    url(r'^', include('tokens.users.urls')),
    url(r'^', include('users.urls')),
]
