from rest_framework.serializers import ModelSerializer

from venues.models import Venue


class VenueSerializer(ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
