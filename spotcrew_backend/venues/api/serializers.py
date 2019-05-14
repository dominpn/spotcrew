from rest_framework_gis.serializers import GeoModelSerializer

from venues.models import Venue


class VenueSerializer(GeoModelSerializer):
    class Meta:
        model = Venue
        geo_field = 'location'
        fields = '__all__'
