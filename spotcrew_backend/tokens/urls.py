from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

from tokens.views import SpotCrewTokenObtainPairView

urlpatterns = [
    url(r'^api/login/$', SpotCrewTokenObtainPairView.as_view(), name='login'),
    url(r'^api/token/refreshing/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
