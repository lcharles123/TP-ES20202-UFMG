from django.db import models

# Create your models here.
class dados_api(models.Model):
    dispositivo=models.ForeignKey('Dispositivo', on_delete=models.SET_NULL,null=True)

    #Criar estrutura que terão os dados aqui