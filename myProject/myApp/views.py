from django.shortcuts import render
from .forms import StudentForm, CourseForm, TeacherForm 

# Create your views here.

# Student view
def view_student(request):
  form = StudentForm()
  if request.method == 'POST':
    # Update the form object with the content of POST
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form': form}
  return render(request, 'add_student.html', context)

# Course View
def view_course(request):
  form = CourseForm()
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form': form}
  return render(request, 'add_course.html', context)

# Teacher views 
def view_teacher(request):
  form = TeacherForm()
  if request.method == 'POST':
    form = TeacherForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form': form}
  return render(request, 'add_teacher.html', context)



