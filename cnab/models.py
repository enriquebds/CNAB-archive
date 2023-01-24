from django.db import models

# Create your models here.
from django.db import models


class UploadArchive(models.Model):
    cnab_archive = models.FileField(upload_to="uploads")


class Cnab(models.Model):
    type = models.CharField(max_length=13)
    date = models.CharField(max_length=8)
    value = models.IntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    time = models.CharField(max_length=8)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)