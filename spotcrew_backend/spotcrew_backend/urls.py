from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^', include('tokens.urls')),
]
