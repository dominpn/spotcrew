from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class SpotCrewTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['type'] = user.type
        return token
