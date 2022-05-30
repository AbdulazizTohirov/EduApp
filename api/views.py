from django.shortcuts import render
from rest_framework import generics
from main import models
from . import serializers


class SubjectCreateView(generics.CreateAPIView):
    queryset = models.SubjectModel.objects.all()
    serializer_class = serializers.SubjectSerializer

