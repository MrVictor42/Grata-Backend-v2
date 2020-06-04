from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from questionnaires.models import Questionnaire
from questionnaires.api.serializers import QuestionnaireSerialize

from questions.api.serializers import QuestionsSerialize
from questions.models import Questions

class QuesttionaireCreateView(CreateAPIView):

    serializer_class = QuestionsSerialize
    queryset = Questions.objects.all()

class QuesttionaireListView(ListAPIView):

    serializer_class = QuestionnaireSerialize
    queryset = Questionnaire.objects.all()

class QuesttionaireDetailView(RetrieveAPIView):

    serializer_class = QuestionnaireSerialize
    queryset = Questionnaire.objects.all()