from rest_framework.serializers import ModelSerializer

from gradedQuesttionaire.models import GradedQuesttionaire

class GradedQuesttionaireSerialize(ModelSerializer):

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')