from django.db import models

# Create your models here.

# Student Model

class Student(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
# Course Model

class Course(models.Model):
  name = models.CharField(max_length=100)
  code = models.CharField(max_length=20, unique=True)
  description = models.TextField(blank=True)
  duration = models.PositiveIntegerField()

  def __str__(self):
    return self.name 


#  Enrollment Model


class Enrollment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollment")
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollment")
  enrollment_at = models.DateTimeField(auto_now_add=True)

  class Meta :
    constraints = [models.UniqueConstraint(fields=["student","course"], name="unique_student_course")]

  def __str__(self):
    return f"{self.student} - {self.course}"  