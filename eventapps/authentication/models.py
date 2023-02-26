from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Create your models here.


class User(AbstractUser):
    is_dei = models.BooleanField(default=False, verbose_name='Director')
    is_adj = models.BooleanField(default=False, verbose_name='Adjunto')
    is_uga = models.BooleanField(default=False, verbose_name='UGA')
    is_uap = models.BooleanField(default=False, verbose_name='UAP')
    is_ucvq = models.BooleanField(default=False, verbose_name='UCVQ')
    is_uedc = models.BooleanField(default=False, verbose_name='UEDC')
    is_secretary = models.BooleanField(
        default=False, verbose_name='Sekretaria')
    is_media = models.BooleanField(default=False, verbose_name='Media')
