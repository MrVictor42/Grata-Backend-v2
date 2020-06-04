from rest_framework.serializers import ModelSerializer

from users.api.serializers import StringSerializer
from questions.models import Questions

class QuestionsSerialize(ModelSerializer):

    choices = StringSerializer(many = True)
    users = StringSerializer(many = True)

    class Meta:

        model = Questions
        fields = ('__all__')