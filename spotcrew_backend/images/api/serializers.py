from rest_framework.serializers import ModelSerializer

from images.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'link',
        )
