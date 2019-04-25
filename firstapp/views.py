from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.
def index(request):
    return HttpResponse("I am in First Application.")

def home(request):
    home= {'home_var' : "THIS IS MY HOMEPAGE"}
    return render(request,'firstapp/index.html', context= home)

def about(request):
    about= {'about_var' : "About"}
    return render(request,'firstapp/index1.html', context= about)

def gallery(request):
    gallery= {'gallery_var' : "Gallery"}
    return render(request,'firstapp/index2.html', context= gallery)

def login(request):
    login= {'login_var' : "login"}
    return render(request, 'firstapp/index4.html', context=login)

def signup(request):
    form = forms.FormName()
    if request.method == "POST":
        if form.is_valid():
            form = forms.FormName(request.POST)
            form.save()
            return HttpResponse("Your Values are saved")
        else:
            print(form.errors)
            return render(request, 'firstapp/index3.html', )
    return render(request,'firstapp/index3.html',{'form1':form})