from django.shortcuts import render
from django.http import HttpResponse
from .models import Countries,Regions
# Create your views here.
# def orm_list(request):
#     countries = Countries.objects.all()
#     print(countries.query)
#     country_list = ""
#     for country in countries:
#         country_list += f"<li>{country.country_name }  </li>"
#     return HttpResponse(f"<ol>{country_list}</ol>")



def index_page(request):

    # return render(request, "index.html")
    return HttpResponse(render(request,"index.html"))