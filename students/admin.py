from django.contrib import admin
from .models import Student, Teacher, Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'expertise')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'teacher')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   
    list_display = ('first_name', 'last_name', 'email')