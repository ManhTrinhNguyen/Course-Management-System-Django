from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# Student Model
class Student(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.EmailField(unique=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  
# Teacher Model 
class Teacher(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  expertise = models.CharField(max_length=200)
  email = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  
# Course Model 
class Course(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  students = models.ManyToManyField(Student, related_name='courses')
  teachers = models.ManyToManyField(Teacher, related_name='courses')
  
  def __str__(self):
    return self.name
  
  def clean(self):
    # Custom validation: A student can not enroll in the same course twice 
    student_ids = self.students.values_list('id', flat=True)
    if len(student_ids) != len(set(student_ids)):
      raise ValidationError('A student can not enroll in the same course twice')
    
    