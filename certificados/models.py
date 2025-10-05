from django.db import models

class certificado(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=200)
    data_emissao = models.DateField()
    arquivo = models.FileField(upload_to='certificados/', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.curso}'
