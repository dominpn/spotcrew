from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SpotCrewTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['type'] = user.type
        return token
