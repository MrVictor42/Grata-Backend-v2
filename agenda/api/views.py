from rest_framework.generics import ListAPIView
from agenda.models import Agenda
from agenda.api.serializers import AgendaSerialize

from meetings.models import Meeting

class AgendaListView(ListAPIView):

    serializer_class = AgendaSerialize
    queryset = Agenda.objects.all()

class AgendasMeeting(ListAPIView):

    serializer_class = AgendaSerialize

    def get_queryset(self):

        meeting_id = self.kwargs['pk']
        current_meeting = Meeting.objects.get(id = meeting_id)
        list_agendas_meeting = current_meeting.agendas.all()

        return list_agendas_meeting