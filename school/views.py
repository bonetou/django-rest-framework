from django.db.models import query
from rest_framework import serializers, viewsets
from school.models import Student, Course
from .serializer import StudentSerializer, CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    '''Shows all students'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    '''Show all courses'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    