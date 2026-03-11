from django.urls import path
from .views import shelf , book

urlpatterns = [
    path('',shelf, name="bookshelf"),
    path('<int:book_id>/',book, name="book"),
]