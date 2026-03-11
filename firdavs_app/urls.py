from django.urls import path
from .views import *
urlpatterns = [
    path('',customer_form,name="customer_form"),
    path('lists/',customer_list,name="customer_list"),
]