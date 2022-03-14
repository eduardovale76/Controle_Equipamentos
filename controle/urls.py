from django.contrib import admin
from django.urls import path, include
from equipamento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamento/', include('equipamento.urls')),
    path('auth/', include('usuarios.urls')),
    path('accounts/', include('allauth.urls')),
]
