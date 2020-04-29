from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from images.models import Image
from sectors.models import Sector

class User(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length = 20, unique = True)
    email = models.EmailField(max_length = 50, unique = True)
    is_administrator = models.BooleanField(default = False)
    is_participant = models.BooleanField(default = False)
    ramal = models.CharField(max_length = 6)
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 500, null = True)
    image = models.ForeignKey(Image, on_delete = models.CASCADE, related_name = 'image_user',
                              null = True, blank = True)
    sector = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'users_in_sector',
                               null = True, blank = True)
    is_staff = models.BooleanField(_('staff status'), default = False)
    is_active = models.BooleanField(_('active status'), default = False)
    is_superuser = models.BooleanField(_('superuser status'), default = False)

    def __str__(self):
        return self.name

class Participant(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username