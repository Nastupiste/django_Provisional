from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
# fmt: off
urlpatterns = [
    path('provisional/admin/productos/nuevo', NuevoProducto.as_view(), name='nuevo'),
    path('provisional/admin/productos/listado', Listar.as_view(), name='listado'),
    path('provisional/admin/productos/<pk>', Detalles.as_view(), name='detalles'),
    path('provisional/admin/productos/<pk>/edicion', Editar.as_view(), name='edicion'),
    path('provisional/admin/productos/<pk>/eliminar', Eliminar.as_view(), name='eliminar'),
]
# fmt: on