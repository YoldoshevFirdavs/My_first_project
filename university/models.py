from django.db import models
from django.db.models import ManyToManyField, ForeignKey

# Create your models here.
#bularni yozish osson buldi juda ham ossssson buldi

class University(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    capacity_students = models.IntegerField(default=0,null=True,blank=True)


    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    # universitet o'chirilsa undagi fakultetlar ham disappear bo'ladi, shuning uchun on_delete=models.CASCADE ishlatdim : unversitet uchirildi fakultetlar quladi hammasi bir aytda simultaneously o'chadi
    # simultaneously : bir paytda , bir vaqtda degani
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='faculties') # foreign key ishlatishimning sababi :
    # har bir fakultet bitta universitetga tegishli bo'ladi, on_delete=models.CASCADE esa universitet o'chirilsa fakultetlar ham o'chib ketadi,
    """
    related_name — bu teskari bog'lanish uchun o'zimiz qo'ygan 'ism'. 
    Masalan, bitta universitetda ko'p fakultetlar bor. Universitet obyektidan turib uning barcha fakultetlarini olish uchun university.faculties.all() deb yozsam buldi hehe. 
    Agar bu nomni qo'ymaganimda, Django avtomatik ravishda university.faculty_set.all() degan xunukroq nom bergan bo'lardi.Bu esa menga yoqmadi shu uchun ai dan suradim va u shuni tavsiya qildi
    Men esa kod chiroyli bo'lishi uchun o'zim nomladim nomlarni www.
    """


    def __str__(self):
        return f"{self.name} ({self.university.name})"


class Course(models.Model):

    name = models.CharField(max_length=200)

    # Fakultet o'chsa undagi  kurslar ham o'chib ketadi,bu lar ham simultaneously o'chadi

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='courses') # foreign key ishlatishimning sababi :

    # har bir kurs bitta fakultetga tegishli bo'ladi,
    # on_delete=models.CASCADE esa fakultet o'chirilsa kurslar ham o'chib ketadi,
    # related_name='courses' esa reverse relation uchun kerak bo'ladi yani faculty.courses orqali kurslarga murojaat qilishimiz mumkin bo'ladi


    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True) # 1 ta teacherni 1000 takursga 1 ta kursda 1000 ta teacher bulishi mukin shu uchun manytomany


    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    courses = models.ManyToManyField(Course, related_name='students', blank=True) # 1 ta student 1000 ta kursga yozilishi mumkin, 1 ta kursda 1000 ta student bo'lishi mumkin, shu uchun manytomany
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')


    def __str__(self):
        return self.name
