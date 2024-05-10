from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.

def login (request):
    
    api_base_url = 'https://rest-framework-login.vercel.app/'
    login_url = api_base_url + 'login/'
    
    response = requests.post(login_url, data=
                             {
            "username": "felipemadeit",
            "password": "IdeaTab2005"
            })
    
    if response.status_code == 200:
        print("Inicio de sesion exitosa")
    else:
        print("Login fallido")
        
def register (request):
    
    api_base_url = 'https://rest-framework-login.vercel.app/'
    register_url = api_base_url  + 'register/'
    
    response = requests.post(register_url, data= {
        "username": "julian",
        "email": "julian@gmail.com",
        "password": "IdeaTab"
    })
    
    if response.status_code == 200:
        print("Registro exitoso")
    else:
        print("Login fallido")



    
    