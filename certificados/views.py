from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
import base64

from .serializers import CertificadoSerializer
from .utils import gerar_pdf_certificado

class GerarCertificadoView(APIView):
    def post(self, request):
        serializer = CertificadoSerializer(data=request.data)
        if serializer.is_valid():
            dados = serializer.validated_data
            
            nome = dados['nome']
            curso = dados['curso']
            data_emissao = dados['data_emissao'].strftime('%d/%m/%Y')
            
            arquivo_nome = f'{nome.replace(" ", "_")}_certificado.pdf'
            caminho_arquivo = gerar_pdf_certificado(nome, curso, data_emissao, arquivo_nome)
            
            certificado = serializer.save(arquivo=caminho_arquivo)
            caminho_absoluto = os.path.join(settings.MEDIA_ROOT, caminho_arquivo)

            if os.path.exists(caminho_absoluto):
                with open(caminho_absoluto, 'rb') as pdf_file:
                    pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')
                
                resposta =  {
                    "id": certificado.id,
                    "nome": certificado.nome,
                    "curso": certificado.curso,
                    "data_emissao": str(certificado.data_emissao),
                    "link_pdf": settings.MEDIA_URL + caminho_arquivo,
                    "pdf_base64": pdf_base64
                }   

                return Response(resposta, status=status.HTTP_201_CREATED)

            return Response({"erro": "Arquivo gerado, mas não encontrado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)