from django.urls import path
from .views import DayCreateView, DayDetailView, GroupCreateView, GroupDetailView, SubjectCreateView, SubjectDetailView
from main.models import SubjectModel


urlpatterns = [
    path('subject/create/', SubjectCreateView.as_view()),
    path('Subject/detail/<int:pk>/', SubjectDetailView.as_view()),
    path('day/create/', DayCreateView.as_view()),
    path('day/detail/<int:pk>/', DayDetailView.as_view()),
    path('group/create/', GroupCreateView.as_view()),
    path('group/detail/<int:pk>/', GroupDetailView.as_view())
]