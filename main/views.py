from django.shortcuts import render
from django.shortcuts import redirect,render
from.models import *


def index_view(request):
    users = User.objects.all()
    subject_model = SubjectModel.objects.all()
    context = {
        'users':users,
        'subject': subject_model
    }
    return render(request, 'index.html', context)