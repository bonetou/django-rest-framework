from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    student_number = models.CharField(max_length=6)
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B', 'BASIC'),
        ('I', 'INTERMEDIARY'),
        ('A', 'ADVANCED'),
    )
    course_id = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    
    def __str__(self):
        return self.description
    
class Registration(models.Model):
    TIME = (
        ('M', 'MORNING'),
        ('E', 'EVENING'),
        ('N', 'NIGHT'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.CharField(max_length=1, choices=TIME, blank=False, null=False, default='M')