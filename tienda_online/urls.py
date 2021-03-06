"""tienda_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.contrib import admin
from django.urls import path
from inventario.views import *
from contacto.views import mensaje_contacto
from inicio.views import inicio
from ventas.views import ventas, fectura
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,name= 'inicio'),
    path('busqueda_productos/', vista_busqueda_productos),
    path('obtener_producto/', obtener_producto),
    path('agregar_producto/', agregar_producto, name='add-prods'),
    path('mostrar_productos/', mostrar_productos, name='show-prods'),
    path('editar_producto/<int:pk>', editar_producto, name='edit-prods'),
    path('eliminar_producto/<int:pk>', eliminar_producto, name='del-prods'),
    path('ventas/<int:pk>', ventas, name='ventas'),
    path('contacto/', mensaje_contacto),
    path('fectura/', fectura, name='fectura')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
