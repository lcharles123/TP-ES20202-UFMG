from django.db import models

# Classe principal, onde se encontra todos os links
class Links(models.Model):
    userName =  models.CharField( max_length=20, help_text='usuario associado:')
    nomeLink = models.CharField( max_length=20, help_text='Nome do Link:') 
    chaveLink = models.CharField(max_length=100, default='', editable=False) 

    # Métodos
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.nomeLink

class Dispositivos(models.Model):
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE) #para preservar os dados de dispositivos
    timeStamp = models.DateField(auto_now_add=True)
    dado = models.IntegerField( help_text='dado')

    class Meta:
        ordering = ['-timeStamp']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.my_field_name



