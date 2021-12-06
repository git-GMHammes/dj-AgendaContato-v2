from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.exibeContato, name='exibeContato'), 
    # contato_id - Pode ser qualquer variável
    # exibeContato - Pode ser qualquer variável que será criado na(o)exibeContato
]
