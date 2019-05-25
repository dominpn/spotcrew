from django_filters import rest_framework as filters
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response

from events.models import Event
from events.api.permissions import IsOwnerAdminOrReadOnly
from events.api.serializers import EventSerializer, EventAttendanceSerializer
from events.api.filters import EventFilter


class EventListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EventSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.all()

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


class EventAttendanceView(mixins.CreateModelMixin, generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventAttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = Event.objects.get(event_id=self.lookup_field, user_id=self.request.user)
        if instance is None:
            return Response('Attendance not found', status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)

    def perform_create(self, serializer):
        event = Event.objects.get(event_id=self.lookup_field)
        serializer.save(event_id=event, user_id=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
