from django.urls import path
from django.views.generic import TemplateView

app_name = 'mensajes'

urlpatterns = [
    path('',
         TemplateView.as_view(template_name='mensajes/index.html'),
         name='index'
         ),
    path('recibidos/',
          TemplateView.as_view(template_name='mensajes/recibidos.html'),
          name='recibidos'
          )
]