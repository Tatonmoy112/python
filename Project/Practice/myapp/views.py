from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "Tanvir",
        "age": 23,
        "national": "BD"
    }
    
    return render(request, "index.html", context)
