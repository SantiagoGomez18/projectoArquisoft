from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PacienteForm
from .logic.pacienteLogic import getPacientes, createPaciente

def pacienteList(request):
    pacientes = getPacientes()
    context = {
        pacienteList: pacientes
    }
    return render(request, 'paciente/pacienteList.html', context)

def pacienteCreate(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            createPaciente = form
            messages.success(request, 'Paciente creado exitosamente')
            return HttpResponseRedirect(reverse('pacienteList'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()
    
    context = {
        'form':form,
    }
    return render(request, 'paciente/pacienteCreate.html', context)

