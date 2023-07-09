"""TPO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views
#import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

#se configuran las rutas con el patron 'xxxx/' que mapea la vista xxxx y le asigno un nombre

urlpatterns = [
#    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.index, name='index'),
    path('vender/', views.ventas, name='vender'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('contacto/', views.contacto, name='contacto'),
    path('vender/productos/', views.venta_productos, name='vender_productos'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
