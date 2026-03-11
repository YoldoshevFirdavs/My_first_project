from django.shortcuts import render, redirect

from firdavs_app.forms import CustomerForm


# Create your views here.

def customer_form(request):
    form = CustomerForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("customers-list")
    ctx = {
        "form":form
    }
    return render(request, "form.html",ctx)

def customer_list(request):
    print(("hi"))




