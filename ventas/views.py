from multiprocessing import context
from django.shortcuts import render

from inventario.models import Productos

# Create your views here.
def ventas (request,pk):
    producto = Productos.objects.get(id=pk)
    context = {
        'producto':producto
    }
    return render (request,"ventas.html",context)