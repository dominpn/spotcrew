from django.contrib.gis.geos import Point
from rest_framework import generics, mixins

from venues.models import Venue
from venues.api.serializers import VenueSerializer


class VenueListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VenueSerializer
    query_parameters = ()

    def get_queryset(self):
        result = Venue.objects.all()
        if self.request.GET.get('longitude') and self.request.GET.get('latitude') and self.request.GET.get('radius'):
            location = Point(float(self.request.GET['longitude']), float(self.request.GET['latitude']))
            # TODO
            # https://stackoverflow.com/questions/24194710/geodjango-dwithin-errors-when-using-django-contrib-gis-measure-d
            #
            # radius = float(self.request.GET['radius'])
            # result = result.filter(location__dwithin=(location, Distance(km=radius)))

            radius = float(self.request.GET['radius']) / 111.325
            result = result.filter(location__distance_lte=(location, radius))

        for filter_field in self.query_parameters:
            if self.request.GET.get(filter_field):
                result = result.filter(**{filter_field: self.request.GET[filter_field]})
        return result

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class VenueDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = VenueSerializer
    # TODO permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Venue.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
