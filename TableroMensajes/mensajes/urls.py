from django.urls import path
from .views import ver_mensajes, index

app_name = 'mensajes'

urlpatterns = [
    path('', index,name='index'),
    path('recibidos/', ver_mensajes, name='ver_mensajes'),
]