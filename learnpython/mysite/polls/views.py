from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index1.html')

#return HttpResponse('<h1> Hey, well come to my site</h1>')