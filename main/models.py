from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=255)
    subject = models.ForeignKey(
        'SubjectModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )  
    tajriba = models.PositiveIntegerField(blank=True, null=True)
    group = models.ForeignKey(
        'GroupModel', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    img = models.ImageField(upload_to = 'users')

    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


class SubjectModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DayModel(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class GroupModel(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
    days = models.ForeignKey(DayModel, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title