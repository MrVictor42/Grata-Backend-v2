from rest_framework.serializers import ModelSerializer

from projects.models import Project

from users.api.serializers import StringSerializer

class ProjectSerialize(ModelSerializer):

    users = StringSerializer(many = True)

    class Meta:

        model = Project
        fields = ('__all__')
        lookup_field = 'slug'