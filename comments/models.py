from django.db import models

from users.models import User
from meetings.models import Meeting

class Comment(models.Model):

    description = models.CharField(max_length = 400)
    meeting = models.ForeignKey(Meeting, on_delete = models.CASCADE,
                                related_name = 'meeting_comments', null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,
                                related_name='user_comments', null = True, blank = True)