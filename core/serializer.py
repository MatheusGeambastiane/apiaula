from rest_framework import serializers
from . import models

class Filmes(serializers.ModelSerializer):
    class Meta:
        model = models.Filme
        fields = '__all__'
        