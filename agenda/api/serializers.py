from rest_framework.serializers import ModelSerializer

from agenda.models import Agenda

class AgendaSerialize(ModelSerializer):

    class Meta:

        model = Agenda
        fields = ('__all__')