from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import minha_tarefa

def home(request):
    print(minha_tarefa.delay())
    return HttpResponse('<h1>Estou na home</h1>')
