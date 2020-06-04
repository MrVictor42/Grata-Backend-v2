from django.db import models

from users.models import User
from choices.models import Choice
from questions.models import Questions, Questionnaire

class GradedQuesttionaire(models.Model):

    status = models.BooleanField(default = False)
    rate = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'answer_user',
                             null = True, blank = True)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_choice',
                               null = True, blank = True)
    question = models.ForeignKey(Questions, on_delete = models.CASCADE, related_name = 'answer_quiz',
                             null = True, blank = True)
    questtionaire = models.ForeignKey(Questionnaire, models.CASCADE, related_name = 'answer_questtionaire',
                                      null = True, blank = True)