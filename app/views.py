from django.shortcuts import render  

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def notes(request):
    return render(request, 'notes.html')

def account(request):
    return render(request, 'account.html')
# Create your views here.
