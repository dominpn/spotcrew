from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

from spotcrew_backend.tokens.views import SpotCrewTokenObtainPairView

urlpatterns = [
    path(r'api/token/$', SpotCrewTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refreshing/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
