from django.db.models import query
from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from .serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationsStudentSerializer, ListRegistrationsCourseSerializer

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
    
class ListRegistrationsStudent(generics.ListAPIView):
    '''Lists an student's registrations'''
    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs['pk'])
    serializer_class = ListRegistrationsStudentSerializer

class ListRegistrationsCourse(generics.ListAPIView):
    '''Lists an course's registrations'''
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs['pk'])
    serializer_class = ListRegistrationsCourseSerializer

