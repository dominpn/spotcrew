from rest_framework import generics, mixins

from events.models import Event
from events.api.permissions import IsOwnerAdminOrReadOnly
from events.api.serializers import EventSerializer


class EventListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EventSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]
    query_parameters = (Event.event_start, )

    def get_queryset(self):
        result = Event.objects.all()
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


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
