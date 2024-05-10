from django.shortcuts import render

# Create your views here.

def home_store (request):
    return render (request, 'home_store.html')
