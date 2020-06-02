from rest_framework.serializers import ModelSerializer

from choices.models import Choice

class ChoiceSerialize(ModelSerializer):

    class Meta:

        model = Choice
        fields = ('__all__')