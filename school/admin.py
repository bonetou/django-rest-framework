from django.contrib import admin
from school.models import Student, Course, Register

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'student_number', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'description', 'level')
    list_display_links = ('id', 'course_id')
    search_fields = ('course_id',)
    list_per_page = 20

admin.site.register(Course, Courses)

class Registers(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'time')
    list_display_links = ('id', )

admin.site.register(Register, Registers)
