from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def index(request):
    return HttpResponse('<h1> Hey, well come to my site</h1>')'''

def homepage(request):
     return render(request, 'index.html')