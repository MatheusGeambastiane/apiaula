from django.shortcuts import render
from rest_framework import viewsets
from . import serializer
from . import models


class FilmesViewSets(viewsets.ModelViewSet):
    serializer_class = serializer.Filmes
    queryset = models.Filme.objects.all()

# Create your views here.


