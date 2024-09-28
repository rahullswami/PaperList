from django.shortcuts import render
from .models import *

# Create your views here.
def Index(request):
    paper_models = Paper_Models.objects.all()

    return render(request, 'index.html', {'papers': paper_models})

def Category_page(request):
    return render(request, 'category.html')

def Nots_page(request):
    return render(request, 'notes.html')

def Contact_us(request):
    return render(request, 'contact.html')