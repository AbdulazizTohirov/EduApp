from django.shortcuts import render
from rest_framework import generics
from main import models
from . import serializers


class SubjectCreateView(generics.CreateAPIView):
    queryset = models.SubjectModel.objects.all()
    serializer_class = serializers.SubjectSerializer


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SubjectModel.objects.all()
    serializer_class = serializers.SubjectSerializer


class DayCreateView(generics.CreateAPIView):
    queryset = models.DayModel.objects.all()
    serializer_class = serializers.DaySerializer


class DayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DayModel.objects.all()
    serializer_class = serializers.DaySerializer

class GroupCreateView(generics.CreateAPIView):
    queryset = models.GroupModel.objects.all()
    serializer_class = serializers.GroupSerializer
    
class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.GroupModel.objects.all()
    serializer_class = serializers.GroupSerializer
