from rest_framework.serializers import ModelSerializer

from sports.models import Sport


class SportSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'
