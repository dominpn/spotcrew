from rest_framework import generics, mixins

from venues.models import Venue
from venues.api.serializers import VenueSerializer


class VenueListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VenueSerializer
    query_parameters = ()

    def get_queryset(self):
        result = Venue.objects.all()
        for filter_field in self.query_parameters:
            if self.request.GET.get(filter_field):
                result = result.filter(**{filter_field: self.request.GET[filter_field]})
            return result

    def perform_create(self, serializer):
        serializer.save()

    # TODO ??
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
