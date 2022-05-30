from django.urls import path
from .views import SubjectCreateView


urlpatterns = [
    path('subject/create/', SubjectCreateView.as_view())
]