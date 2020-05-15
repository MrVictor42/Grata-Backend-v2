from rest_framework.serializers import ModelSerializer

from meetings.models import Meeting

from users.api.serializers import StringSerializer

class MeetingSerialize(ModelSerializer):

    users = StringSerializer(many = True)

    class Meta:

        model = Meeting
        fields = ('__all__')
        lookup_field = 'slug'