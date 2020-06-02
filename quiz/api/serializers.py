from rest_framework.serializers import ModelSerializer

from users.api.serializers import StringSerializer
from quiz.models import Quiz

class QuizSerialize(ModelSerializer):

    choices = StringSerializer(many = True)
    users = StringSerializer(many = True)

    class Meta:

        model = Quiz
        fields = ('__all__')