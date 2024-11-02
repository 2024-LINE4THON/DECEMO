from django.urls import path
from .views import calendar_view, question_detail

urlpatterns = [
    path('calendar/', calendar_view, name='calendar'),
    path('answer/<int:day>/', question_detail, name='question_detail'),
]
