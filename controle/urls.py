from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamento/', include('equipamento.urls')),
    path('auth/', include('usuarios.urls'))
]
