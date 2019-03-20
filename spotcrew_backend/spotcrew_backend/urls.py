from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^', include('events.urls')),
    url(r'^', include('tokens.urls')),
]
