from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.base, name='base'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('logado', views.logado, name='logado'),
    path('curso', views.curso, name='curso'),
    path('cronograma', views.cronograma, name='cronograma'),
    path('perguntas', views.perguntas, name='perguntas'),


]
