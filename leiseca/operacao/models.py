from django.db import models

# Create your models here.
class Efetivo(models.Model):
    date_servico = models.DateTimeField('date published')
    chefe_civil = models.CharField(max_length=30)
    chefe_militar = models.CharField(max_length=30)
    segov_registro_um = models.CharField(max_length=30)
    segov_registro_dois = models.CharField(max_length=30)
    segov_filmagem = models.CharField(max_length=30)
