from rest_framework import viewsets
from .models import Student, Teacher, Course
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer
from django.http import HttpResponse

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



def welcome_view(request):
    return HttpResponse("""
        <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
            <h1 style="color: #2c3e50;">🎓 SmartEdu API'ye Hoş Geldiniz</h1> <br></br>
            
            <div style="margin-top: 20px;">
                <a href="/api/" style="padding: 10px 20px; background: #3498db; color: white; text-decoration: none; border-radius: 5px;">API Listesine Git</a>
                <a href="/admin/" style="padding: 10px 20px; background: #2ecc71; color: white; text-decoration: none; border-radius: 5px; margin-left: 10px;">Yönetim Paneline Git</a>
            </div>
            <p style="margin-top: 30px; color: #7f8c8d; font-size: 0.9em;">Dockerize & JWT Secured Backend</p>
        </div>
    """)
