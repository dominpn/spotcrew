from rest_framework_gis.serializers import GeoModelSerializer

from images.api.serializers import ImageSerializer
from images.models import Image
from venues.models import Venue


class VenueSerializer(GeoModelSerializer):
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Venue
        geo_field = 'location'
        fields = '__all__'

    def create(self, validated_data):
        images_links = validated_data.pop('images')
        venue = Venue.objects.create(**validated_data)

        for image_link in images_links:
            image, created = Image.objects.get_or_create(link=image_link['link'])
            venue.images.add(image)
        return venue

    def update(self, instance, validated_data):
        images_links = validated_data.pop('images')

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)

        images_list = []

        for image in images_links:
            link, created = Image.objects.get_or_create(link=image['link'])
            images_list.append(link)

        instance.images.set(images_list)
        instance.save()
        return instance
