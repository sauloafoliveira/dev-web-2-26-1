from django.shortcuts import render
import random
from .models import Country

# Create your views here.

def index_bc(req):
    n_chaves = random.randint(100, 10_000)
    logado = random.random() > 0.5
    paises = Country.objects.all()

    return render(req, "index_bc.html", {
        'n_chaves': n_chaves / 5,
        'logado': logado,
        'paises': paises
    })