from django import forms
from .models import Student, Teacher, Course 

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'

class TeacherForm(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = '__all__'

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = '__all__'

  def clean(self):
    cleaned_data = super().clean()
    students = cleaned_data.get('students')

    if students and len(students) != len(set(students)):
      raise forms.ValidationError('A student can not enroll the same course more than once')
    
    return cleaned_data

