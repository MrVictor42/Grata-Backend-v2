from rest_framework.generics import ListAPIView
from rules.models import Rules
from rules.api.serializers import RulesSerialize

from meetings.models import Meeting

class RulesListView(ListAPIView):

    serializer_class = RulesSerialize
    queryset = Rules.objects.all()

class RulesMeeting(ListAPIView):

    serializer_class = RulesSerialize

    def get_queryset(self):

        meeting_id = self.kwargs['pk']
        current_meeting = Meeting.objects.get(id = meeting_id)
        list_rules_meeting = current_meeting.rules.all()

        return list_rules_meeting