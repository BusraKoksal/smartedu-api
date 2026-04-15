from rest_framework import serializers
from .models import Student, Teacher, Course

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','name','expertise']

class CourseSerializer(serializers.ModelSerializer):
    # Teacher bilgisini de içine göm (Nested Serializer)
    teacher=TeacherSerializer(read_only=True)
    teacher_id= serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), source='teacher', write_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'teacher_id']

class StudentSerializer(serializers.ModelSerializer):
    # Kayıtlı olduğu derslerin sadece isimlerini görelim
    courses = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'courses']