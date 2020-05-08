from django.db import models

from sectors.models import Sector
from users.models import User

class Project(models.Model):

    title = models.CharField(max_length = 40)
    status = models.CharField(max_length = 14)
    slug = models.SlugField(max_length = 100, unique = True, null = True, blank = True)
    sector = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'projects_in_sector',
                               null = True, blank = True)
    users = models.ManyToManyField(User, blank = True, null = True)

    def __str__(self):
        return self.title