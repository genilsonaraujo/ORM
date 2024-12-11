"""
URL configuration for projetointegrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from django.contrib import admin #cria o painel admin com a biblioteca python
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
#from .api_views import ProdutoListCreateAPIView, ProdutoDetailAPIView, SaidaList, SaidaDetail, CurvaABCView
#from .views import lista_produtos, cria_produto
from django.conf import settings
from django.conf.urls.static import static
#from .views import busca_produtos



urlpatterns = [ #ROTAS
    path('', views.index, name='index'),# insere index funçao dentro de views
    path('topics', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),#rota para views
    path('home', views.home, name='home'),# insere nome= home  funçao dentro de views
    path('new_topic', views.new_topic, name='new_topic'),# insere NewTopic na views, foi criada para formulario
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'), #depois crie essa função na view
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('cria_produto/', views.cria_produto, name='cria_produto'),
    path('remove_produto/<int:produto_id>/', views.remove_produto, name='remove_produto'),
    path('produto/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('criar/', views.criar_item, name='criar_item'),
    path('cria/', views.criar_ups, name='criar_ups'),
    #path('lista_saida/', views.lista_saida, name='lista_saida'),
    #path('adicionar_saida/', views.adicionar_saida, name='adicionar_saida'),
    #path('detalhes_saida/<int:pk>/', views.detalhes_saida, name='detalhes_saida'),
    #path('registrar_saida/', views.registrar_saida, name='registrar_saida'),
    #path('remover_saida/<int:saida_id>/', views.remover_saida, name='remover_saida'),
    
    path('busca_produtos/', views.busca_produtos, name='busca_produtos'),
    path('detalhes/<int:pk>/', views.detalhes_item, name='detalhes_item'),  # URL para detalhes
    path('detalhe/<int:pk>/', views.detalhes_ups, name='detalhes_ups'),

    path('editar_ups/<int:pk>/', views.editar_ups, name='editar_ups'),
    path('excluir_ups/<int:pk>/', views.excluir_ups, name='excluir_ups'),

    path('ups/', views.ups_list, name='ups_list'),  # Lista de UPS
    path('ups/<int:pk>/', views.ups_detail, name='ups_detail'),  # Para detalhes de uma UPS específica

    path('download_relatorio/', views.download_relatorio, name='download_relatorio'),
    
    #path('produte/', ProdutoListCreateAPIView.as_view(), name='produto-list-create'),#API, Dá um nome à rota para facilitar sua referência em outras partes do código, como templates ou redirecionamentos.
    #path('produte/<int:pk>/', ProdutoDetailAPIView.as_view(), name='produto-detail'),#rota produto id
    #path('saidas/', SaidaList.as_view(), name='saida-list'),
    #path('saidas/<int:pk>/', SaidaDetail.as_view(), name='saida-detail'),
    # urls.py
    #path('curva-abc/', CurvaABCView.as_view(), name='curva-abc'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)