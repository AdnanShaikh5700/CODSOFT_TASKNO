from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Student, Course, Enrollment
from .serializers import (StudentSerializer, CourseSerializer, EnrollmentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [AllowAny]

  search_fields = ["name", "email", "phone"]
  ordering_fields = ["name", "email", "created_at"]
  filterset_field = ["name"]


class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  permission_classes = [AllowAny]

  search_fields = ["name", "code"]
  ordering_fields = ["name", "duration"]
  filterset_field = ["code"]


class EnrollmentViewSet(viewsets.ModelViewSet):
  queryset = Enrollment.objects.select_related("student", "course").all()
  serializer_class = EnrollmentSerializer
  permission_classes = [AllowAny]

  filterset_fields = ["student", "course"]
  ordering_fields = ["enrolled_at"]