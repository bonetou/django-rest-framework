from django.db.models import fields
from rest_framework import serializers
from school.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_number', 'birthday']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []

class ListRegistrationsStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['course', 'time']
    course = serializers.ReadOnlyField(source='course.description')
    time = serializers.SerializerMethodField()
    def get_time(self, obj):
        return obj.get_time_display()

class ListRegistrationsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['student', 'time']
    student = serializers.ReadOnlyField(source='student.name')
    time = serializers.SerializerMethodField()
    def get_time(self, obj):
        return obj.get_time_display()