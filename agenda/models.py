from django.db import models

class Agenda(models.Model):

    title = models.CharField(max_length = 40)

    def __str__(self):
        return self.title