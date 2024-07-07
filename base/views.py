from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def getUser(request):
    return render(request, 'getuser.html')
def add(request):
    return render(request, 'adduser.html')