from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from questionnaires.models import Questionnaire
from questionnaires.api.serializers import QuestionnaireSerialize

from quiz.api.serializers import QuizSerialize
from quiz.models import Quiz


class QuesttionaireCreateView(CreateAPIView):
    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()

class QuesttionaireListView(ListAPIView):
    serializer_class = QuestionnaireSerialize
    queryset = Questionnaire.objects.all()

class QuesttionaireDetailView(RetrieveAPIView):
    serializer_class = QuestionnaireSerialize
    queryset = Questionnaire.objects.all()