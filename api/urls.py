from django.urls import path
from .views import SubjectCreateView
from main.models import SubjectModel


urlpatterns = [
    path('subject/create/', SubjectCreateView.as_view())
]