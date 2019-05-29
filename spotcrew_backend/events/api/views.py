from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response

from events.models import Event, EventAttendance
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        EventAttendance.objects.filter(event_id=instance).delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class EventAttendanceView(mixins.CreateModelMixin, generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventAttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = EventAttendance.objects.get(
                event_id=self.kwargs.get(self.lookup_field),
                user_id=self.request.user,
            )
        except ObjectDoesNotExist:
            return Response({'non_field_errors': 'Attendance not found'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        event = Event.objects.get(event_id=self.kwargs.get(self.lookup_field))
        serializer = self.get_serializer(data={'user_id': self.request.user.id, 'event_id': event.event_id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
