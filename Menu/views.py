from django.shortcuts import render
from .models import Practicas
def home(request):
    return render(request, 'Menu/menu.html')

def page_sc(request):
    practica = Practicas.objects.get(id=1)
    return render(request, 'Pages/sc.html', {'practica': practica})