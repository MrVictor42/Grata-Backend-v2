from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_202_ACCEPTED,
    HTTP_400_BAD_REQUEST
)

from gradedQuesttionaire.models import GradedQuesttionaire
from users.models import User
from questionnaires.models import Questionnaire
from questions.models import Questions
from choices.models import Choice

from gradedQuesttionaire.api.serializers import GradedQuesttionaireSerialize

class GradedQuesttionaireListView(ListAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

class GradedQuesttionaireCreate(CreateAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

    def post(self, request, *args, **kwargs):

        gradedQuesttionaire = GradedQuesttionaire()
        user = User.objects.get(id = request.data.get('userID'))
        questtionaire = Questionnaire.objects.get(id = request.data.get('questtionaire_id'))
        questions = request.data.get('questionsID')
        answers = request.data.get('answers')

        gradedQuesttionaire.user = user
        gradedQuesttionaire.questtionaire = questtionaire

        for nullQuestion, auxQuestion in enumerate(questions):
            new_questions = Questions.objects.get(id = auxQuestion)
            gradedQuesttionaire.question = new_questions

        for nullAnswers, auxAnswers in enumerate(answers):
            new_choices = Choice.objects.get(id = auxAnswers)
            gradedQuesttionaire.choice = new_choices

        gradedQuesttionaire.status = True
        gradedQuesttionaire.rate = request.data.get('rate')
        gradedQuesttionaire.save()
        serializer = GradedQuesttionaireSerialize(instance = gradedQuesttionaire, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class GradedInQuesttionaire(ListAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

    def get_queryset(self):

        questtionaire_id = self.kwargs['pk']
        graded_questtionaire = GradedQuesttionaire.objects.filter(questtionaire = questtionaire_id)

        return graded_questtionaire

class UserInGraded(RetrieveAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

    def get_queryset(self):

        user_id = self.kwargs['pk']
        graded_questtionaire = GradedQuesttionaire.objects.filter(user = user_id)

        if graded_questtionaire:
            return graded_questtionaire
        else:
            return None