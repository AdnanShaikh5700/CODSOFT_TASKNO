from rest_framework import serializers
from .models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
  class Meta :
    model = Student
    fields = "__all__"

  
  def validate_name(self, value):
    if not value.strip():
      raise
    serializers.ValidationError("Student Name Cannot Be Emty.")
    return value.strip()


  def validate_phone(self, value):
    if not value.isdigit() or not 10 <= len(value) <= 15:
      raise
    serializers.ValidationError("Enter A Valid Phone Number.")
    return value



class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = "__all__"

  def validate_duration(self, value):
    if value <= 0 :
      raise
    serializers.ValidationError("Duration Must Be Greater Then Zero.")
    return value


class EnrollmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Enrollment
    fields = "__all__"

  def validate(self,data):
    student = data.get("student", getattr(self.instance,"student", None))
    course = data.get("course", getattr(self.instance, "course", None))

    if student and course :
      existing = Enrollment.objects.filter(student=student, course=course)

      if self.instance:
        existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
          raise
        serializers.ValidationError("Student Is Already Enrolled In This Course.")
        return data  