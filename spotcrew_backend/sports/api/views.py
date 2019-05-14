from rest_framework import generics, mixins
from rest_framework import permissions

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

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
