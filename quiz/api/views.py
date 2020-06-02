from rest_framework.generics import ListAPIView

from quiz.api.serializers import QuizSerialize
from quiz.models import Quiz

class QuizListView(ListAPIView):

    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()

class QuizDetailView(ListAPIView):

    serializer_class = QuizSerialize

    def get_queryset(self):

        queryset = Quiz.objects.all()
        questtionaire_pk = self.kwargs['pk']

        if questtionaire_pk is not None:
            queryset = queryset.filter(questtionaire = questtionaire_pk)

        return queryset