from django.db import models


 # Classe principal, onde se encontra todos os links
class Links(models.Model):
    nomeLink = models.CharField( max_length=20, help_text='Nome do Link:') 
    chaveLink = models.CharField(primary_key=True, max_length=16, default="", editable=False) 
    dispID = models.ForeignKey('Dispositivos', on_delete=models.SET_NULL, null=True) #para preservar os dados de dispositivos
    
    class Meta:
        ordering = ['-nomeLink']

    # Métodos
    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de Dispositivos."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """ String para representar o objeto MyModelName (no site Admin)."""
        return self.nomeLink

class Dispositivos(models.Model):
    #name = models.CharField(max_length=100)
    """Uma típica classe definindo um modelo, derivada da classe Model."""
    timeStamp = models.DateField(auto_now_add=True,null=True)
    dado = models.IntegerField( help_text='dado')


    # Metadados
    class Meta:
        ordering = ['-timeStamp']

    # Métodos
    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de Dispositivos."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """ String para representar o objeto MyModelName (no site Admin)."""
        return self.my_field_name
    # Campos



from django.contrib.auth.models import AbstractUser


