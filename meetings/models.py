from django.db import models

from users.models import User
from projects.models import Project

class Meeting(models.Model):

    title = models.CharField(max_length = 40)
    subject_matter = models.CharField(max_length = 500)
    status = models.CharField(max_length = 10, null = True)
    initial_date = models.CharField(max_length = 12)
    final_date = models.CharField(max_length = 12, null = True)
    initial_hour = models.CharField(max_length = 10)
    final_hour = models.CharField(max_length = 10, null = True)
    slug = models.SlugField(max_length = 100, unique = True, null = True, blank = True)
    meeting_leader = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'meeting_leader',
                                       null = True, blank = True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'meetings_in_project',
                                null = True, blank = True)
    users = models.ManyToManyField(User, blank = True, null = True)

    def __str__(self):
        return self.title
