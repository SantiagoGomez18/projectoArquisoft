from ..models import Resultados
import random
from django.db import models as md
from django.utils import timezone


def getResultados():
    return Resultados.objects.all()

def getResultado(res_pk):
    resultado = Resultados.objects.get(pk=res_pk)
    return resultado

def createResultado():
    valor = random.uniform(0, 100)
    recomendaciones = ""
    if valor < 50:
        recomendaciones = "Recomendar a menor de 50"
    else:
        recomendaciones = "Recomendar a mayor de 50"
    fechaGeneracion = timezone.now()
    resultado = Resultados(valor=valor, recomendaciones=recomendaciones, fechaGeneracion=fechaGeneracion)
    resultado.save()
    return ()
