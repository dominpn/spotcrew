from rest_framework_simplejwt.views import TokenObtainPairView

from tokens.jwt.models import SpotCrewTokenObtainPairSerializer


class SpotCrewTokenObtainPairView(TokenObtainPairView):
    serializer_class = SpotCrewTokenObtainPairSerializer
