from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request, 'COVID/home.html')

def about(request):
    return render(request, 'COVID/about.html')

