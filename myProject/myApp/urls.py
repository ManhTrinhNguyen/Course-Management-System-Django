from django.urls import path 
from .views import view_course, view_student, view_teacher

urlpatterns = [
  path('course/', view_course),
  path('student/', view_student),
  path('teacher/', view_teacher)
]