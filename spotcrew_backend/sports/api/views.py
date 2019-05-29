from rest_framework import generics, mixins
from rest_framework import permissions, status
from rest_framework.response import Response

from events.models import Event, EventAttendance
from sports.models import Sport
from sports.api.serializers import SportSerializer


class SportListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Sport.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class SportDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Sport.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        events = Event.objects.filter(sport_id=instance)
        for event in events:
            EventAttendance.objects.filter(event_id=event).delete()
        events.delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
