from rest_framework.serializers import ModelSerializer, SerializerMethodField

from events.models import Event, EventAttendance
from users.models import User
from users.api.serializers import UserSerializer


class EventSerializer(ModelSerializer):
    users = SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('users',)

    def get_users(self, event):
        users = User.objects.filter(eventattendance__event_id=event)
        return UserSerializer(users, many=True, context=self.context).data


class EventAttendanceSerializer(ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = '__all__'
