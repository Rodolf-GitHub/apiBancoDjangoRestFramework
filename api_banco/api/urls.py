from django.urls import path, include
from rest_framework import routers
from .views import *


router=routers.DefaultRouter()
router.register(r'usuario',UsuarioViewSet)
router.register(r'persona',PersonaViewSet)
router.register(r'empresa',EmpresaViewSet)
router.register(r'solicitud',SolicitudViewSet)


urlpatterns =[
    path('',include(router.urls))
]