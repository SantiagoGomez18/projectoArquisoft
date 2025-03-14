from django.db import models
from evento.models import Evento


class Resultado(models.Model):
    
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    valor = models.FloatField(null=True, blank=True, default=None)
    recomendaciones = models.CharField(max_length=250)
    fechaGeneracion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Valor {}, Recomendaciones {}, Fecha Generacion {}".format(self.valor, self.recomendaciones, self.fechaGeneracion)
