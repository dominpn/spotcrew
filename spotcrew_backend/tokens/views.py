from rest_framework_simplejwt.views import TokenObtainPairView

from spotcrew_backend.tokens.models import SpotCrewTokenObtainPairSerializer


class SpotCrewTokenObtainPairView(TokenObtainPairView):
    serializer_class = SpotCrewTokenObtainPairSerializer
