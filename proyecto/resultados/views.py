from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ResultadoForm
from .models import Resultado

def resultadosList(request):
    resultados = Resultado.objects.all()
    return render(request, 'resultados/resultados.html', {'resultados': resultados})

def resultado(request ,id):
    resultado = Resultado.objects.get(id=id)
    return render(request, 'resultados/resultado.html', {'resultado': resultado})

def resultadosCreate(request):
    if request.method == 'POST':
        form = ResultadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Resultado creado')
            return HttpResponseRedirect(reverse('resultados:resultadosList'))
        else:
            messages.error(request, 'Error al crear el resultado')
    else:
        form = ResultadoForm()
    return render(request, 'resultados/resultados_form.html', {'form': form})

