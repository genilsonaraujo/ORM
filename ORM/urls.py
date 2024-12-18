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

from django.conf import settings
from django.contrib import admin #cria o painel admin com a biblioteca python
from django.urls import path, include #path é a rota do endereço 
from django.conf.urls.static import static
#from rest_framework_simplejwt.views import ( #para autenticacao React
#   TokenObtainPairView,
#   TokenRefreshView,
#)


urlpatterns = [
    path('admin/', admin.site.urls),#admin
    path('', include('ORMS.urls')), #quando o url estiver  vazio, vai p o meu Url do meu APP
    path('users/', include('users.urls')), #procura a pagina no navegador
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#autenticacao React
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]
