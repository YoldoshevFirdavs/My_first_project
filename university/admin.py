from django.contrib import admin
from .models import University,Faculty,Student,Course,Teacher
# Register your models here.
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
