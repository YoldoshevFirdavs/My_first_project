from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    html = """
    <h1>First Page</h1>
    <p>This is the first page of our Django application.</p>
    """
    return HttpResponse(html)