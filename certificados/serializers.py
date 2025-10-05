from rest_framework import serializers
from .models import certificado

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = certificado
        fields = ['nome', 'curso', 'data_emissao', 'arquivo']