from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from school.views import StudentViewSet, CourseViewSet, RegistrationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('registrations', RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
