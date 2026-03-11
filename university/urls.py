from django.urls import path
from .views import university_list, university_detail, faculty_detail,course_detail, university_teachers, university_students, faculty_students

urlpatterns = [
    path('universities/', university_list, name="university_list"),
    path('universities/<int:university_id>/', university_detail, name="university_detail"),
    path('faculties/<int:faculty_id>/', faculty_detail, name="faculty_detail"),
    path('courses/<int:course_id>/', course_detail, name="course_detail"),
    path('universities/<int:university_id>/teachers/', university_teachers, name="university_teachers"),
    path('universities/<int:university_id>/students/', university_students, name="university_students"),
    path('faculties/<int:faculty_id>/students/', faculty_students, name="faculty_students"),
]