from django.shortcuts import render

def Login(request):
    return render(request, 'core/Login.html')

def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')
