from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request,'index.html')

def invite(request):

    return render(request,'invite.html')

def landing(request):

    return render(request,'landing.html')

def create(request):

    return render(request,'create.html')
