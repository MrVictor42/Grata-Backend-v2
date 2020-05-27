from django.db import models

from users.models import User
from projects.models import Project
from agenda.models import Agenda
from rules.models import Rules

class Meeting(models.Model):

    title = models.CharField(max_length = 40)
    subject_matter = models.CharField(max_length = 500)
    status = models.CharField(max_length = 10, null = True)
    initial_date = models.CharField(max_length = 12)
    real_date = models.CharField(max_length = 12, null = True)
    initial_hour = models.CharField(max_length = 10)
    real_hour = models.CharField(max_length = 10, null = True)
    duration_time = models.CharField(max_length = 10, null = True)
    slug = models.SlugField(max_length = 100, unique = True, null = True, blank = True)
    meeting_leader = models.ForeignKey(User, on_delete = models.CASCADE,
                                       related_name = 'meeting_leader',
                                       null = True, blank = True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE,
                                related_name = 'meetings_in_project',
                                null = True, blank = True)
    users = models.ManyToManyField(User, blank = True, null = True)
    rules = models.ManyToManyField(Rules, blank = True, null = True)
    agendas = models.ManyToManyField(Agenda, blank = True, null = True)

    def __str__(self):
        return self.title