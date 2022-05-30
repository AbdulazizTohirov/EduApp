from rest_framework import serializers
from main import models

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectModel
        fields = ['name']

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DayModel
        fields = ['name']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupModel
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email',  'phone', 'img', 'tajriba', 'subject']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email',  'phone', 'img', 'group']