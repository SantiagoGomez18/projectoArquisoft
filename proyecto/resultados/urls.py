from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('resultados/', views.resultadosList, name='resultados'),
    path('resultadocreate/', csrf_exempt(views.resultadosCreate), name='resultadosCreate'),
    path('resultado/<int:id>/', views.resultado, name='resultado'),
]