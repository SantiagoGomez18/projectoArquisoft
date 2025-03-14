from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=None)
    hc = models.CharField(max_length=100)
    
    def __str__(self):
        return "Nombre {}, Edad {}, Historia Clinica {}".format(self.name, self.age, self.hc)
