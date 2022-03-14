from django.contrib import admin
from django.urls import path, include
from pages import urls, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamento/', include('equipamento.urls')),
    path('auth/', include('usuarios.urls')),
    path('accounts/', include('allauth.urls')),
    path("", views.LoginView.as_view(), name="login"),
]
