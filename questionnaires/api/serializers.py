from rest_framework.serializers import ModelSerializer

from questionnaires.models import Questionnaire

class QuestionnaireSerialize(ModelSerializer):

    class Meta:

        model = Questionnaire
        fields = ('__all__')