from ..models import Paciente

def getPacientes():
    return Paciente.objects.all()

def createPaciente(name, age, hc):
    paciente = Paciente(name=name, age=age, hc=hc)
    paciente.save()
    return ()