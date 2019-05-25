from rest_framework.serializers import ModelSerializer

from events.models import Event, EventAttendance


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventAttendanceSerializer(ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = '__all__'
