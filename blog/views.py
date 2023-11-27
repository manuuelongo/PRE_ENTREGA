from django.shortcuts import render

def home(request):
    contexto ={}
    return render (request,'index.html', contexto)