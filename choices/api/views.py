from rest_framework.generics import ListAPIView
from choices.models import Choice
from choices.api.serializers import ChoiceSerialize

class ChoiceListView(ListAPIView):

    serializer_class = ChoiceSerialize
    queryset = Choice.objects.all()

class ChoicesQuestion(ListAPIView):

    serializer_class = ChoiceSerialize

    def get_queryset(self):

        question_id = self.kwargs['pk']
        list_choices = Choice.objects.filter(questions = question_id)

        return list_choices