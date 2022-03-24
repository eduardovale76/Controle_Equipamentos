from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from pages import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamento/', include('equipamento.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)