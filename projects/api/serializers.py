from rest_framework.serializers import ModelSerializer

from projects.models import Project

class ProjectSerialize(ModelSerializer):

    class Meta:

        model = Project
        fields = ('__all__')