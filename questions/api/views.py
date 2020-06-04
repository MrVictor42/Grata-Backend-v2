from rest_framework.generics import ListAPIView, DestroyAPIView

from questions.api.serializers import QuestionsSerialize
from questions.models import Questions

class QuizListView(ListAPIView):

    serializer_class = QuestionsSerialize
    queryset = Questions.objects.all()

class QuizDelete(DestroyAPIView):

    serializer_class = QuestionsSerialize
    queryset = Questions.objects.all()

class QuizDetailView(ListAPIView):

    serializer_class = QuestionsSerialize

    def get_queryset(self):

        queryset = Questions.objects.all()
        questtionaire_pk = self.kwargs['pk']

        if questtionaire_pk is not None:
            queryset = queryset.filter(questtionaire = questtionaire_pk)

        return queryset