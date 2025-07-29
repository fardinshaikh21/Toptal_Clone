from django.shortcuts import redirect,render
from django.http import HttpResponse,HttpRequest

def home(request):  
    return render(request,'home.html')
    #return HttpResponse("Welcome to Toptal")


def freelancer_registration(request):
    return render(request,'freelancer_registration.html')    

def freelancer_login(request):
    return render(request,'freelancer_login.html')    