from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Codigo de la seccion de Vistas
# def title_page(request):
#    return HttpResponse('<h1>Caso de Estudio Measurements</h1>')


def title_page(request):
    fecha = str(datetime.datetime.now())
    return render(request, 'title_page.html', {'fecha': fecha})
