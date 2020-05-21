from django.db import models

class Rules(models.Model):

    title = models.CharField(max_length = 40)

    def __str__(self):
        return self.title