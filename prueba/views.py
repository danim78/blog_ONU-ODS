from django.shortcuts import render

# Create your views here.

def hola_mundo(request):
    template = 'hola_mundo.html'
    contexto = {}
    return render(request, template, contexto)