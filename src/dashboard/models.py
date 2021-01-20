from django.db import models

# Create your models here.
#definindo o modelo da pagina
class MyModelName(models.Model):
    """Uma típica classe definindo um modelo, derivada da classe Model."""

    # Campos
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadados
    class Meta:
        ordering = ['-my_field_name']

    # Métodos
    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """ String para representar o objeto MyModelName (no site Admin)."""
        return self.my_field_name

#Classe para guardar os dados de registro de um usuário
class usuario(models.Model):
    
    id=models.UUIDField(primary_key=True)
    email=models.EmailField()
    
    #todo usuario sera definido por um email
    def __str__(self):
        return self.email
    
class dispositivo(models.Model):
    id=models.UUIDField(primary_key=True)
    nome=models.TextField(max_length=30)
    dono=models.ForeignKey('Usuario',on_delete=models.SET_NULL,null=True)
    link_api=models.TextField()
    
    #todo dispositivo será definido por um id + o email do dono
    def __str__(self):
        return self.id+self.dono