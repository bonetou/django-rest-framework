from django.db.models import query
from rest_framework import serializers, viewsets
from school.models import Student, Course, Registration
from .serializer import StudentSerializer, CourseSerializer, RegistrationSerializer

class StudentViewSet(viewsets.ModelViewSet):
    '''Shows all students'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    '''Show all courses'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    '''Show all registrations'''
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    