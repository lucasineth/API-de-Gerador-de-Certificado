from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from certificados.views import GerarCertificadoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/certificados/', GerarCertificadoView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
