from django.db import models

from choices.models import Choice
from users.models import User
from questionnaires.models import Questionnaire

class Quiz(models.Model):

    title = models.CharField(max_length = 50)
    choices = models.ManyToManyField(Choice, blank = True)
    users = models.ManyToManyField(User)
    order = models.SmallIntegerField(null = True)
    questtionaire = models.ForeignKey(Questionnaire, on_delete = models.CASCADE,
                                      related_name = 'questtionaire_quiz', null = True, blank = True)

    def __str__(self):
        return self.title