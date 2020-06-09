from django.db import models

from users.models import User
from questionnaires.models import Questionnaire

class Comment(models.Model):

    description = models.CharField(max_length = 400)
    questtionaire = models.ForeignKey(Questionnaire, on_delete = models.CASCADE,
                                related_name = 'questtionaire_comments', null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,
                                related_name='user_comments', null = True, blank = True)