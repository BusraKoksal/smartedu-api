from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    expertise= models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Course(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='courses')
    def __str__(self):
        return self.title
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Many-to-Many: Bir öğrenci çok derse, bir ders çok öğrenciye sahip olabilir.
    courses=models.ManyToManyField(Course,related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    

