from django.shortcuts import render
from codigo.models import *
from django.http import HttpResponseRedirect, HttpRequest
import os
from django.contrib import messages
from codigo.forms import FormularioCodigo
from datetime import datetime, timedelta

def Insertar(request):
    if request.method=='POST':
        f = FormularioCodigo(request.POST)
        if f.is_valid():
            form = f.save(commit=False)
            form.save()
            messages.info(request, 'Insertado correctamente.')
            return HttpResponseRedirect('/'+str(form.url))
    else:
        f = FormularioCodigo()
    context = {'f':f,}
    return render(request, 'formulario.html', context)


def Editar(request, url):
    c = Codigo.objects.get(url=url)
    if request.method=='POST':
        f = FormularioCodigo(request.POST, instance=c)
        if f.is_valid():
            form = f.save(commit=False)
            form.save()
            messages.info(request, 'Editado correctamente.')
            return HttpResponseRedirect('/'+str(form.url))
    else:
        f = FormularioCodigo(instance=c)
    context = {'f':f,}
    return render(request, 'formulario.html', context)



def Detalles(request, url):
    try:
        c = Codigo.objects.get(url=url)
        ahora = datetime.now()

        y = c.fecha.year
        m = c.fecha.month
        d = c.fecha.day
        h = c.fecha.hour
        i = c.fecha.minute
        s = c.fecha.second

        y1 = ahora.year
        m1 = ahora.month
        d1 = ahora.day
        h1 = ahora.hour
        i1 = ahora.minute
        s1 = ahora.second


        context = {
            'c':c,
        }
        return render(request, 'index.html', context)



    except:
        messages.info(request, 'No encuentro este código. Lo siento.')
        return HttpResponseRedirect('/')



def Eliminar(request, url):
    try:
        c = Codigo.objects.get(url=url)
        c.delete()
        messages.info(request, 'Eliminado Correctamente.')
    except:
        messages.info(request, 'No encuentro este código. Lo siento.')
    return HttpResponseRedirect('/')


def handler404(request):
    messages.info(request, 'No encuentro esa URL. Por favor intente nuevamente.')
    return HttpResponseRedirect('/')

def handler500(request):
    messages.info(request, 'No encuentro esa URL. Por favor intente nuevamente.')
    return HttpResponseRedirect('/')