from django.db import models

# Create your models here.
class Filme(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nome do filme", blank=False, null=False)
    genero = models.CharField(max_length=50)
    