from django.contrib import admin

# Register your models here.
#registrar os modelos para administracao do site



# apenas testando o registro de um modelo contido no arquivo models.py que eh uma classe python

from dashboard.models import MyModelName

admin.site.register(MyModelName)




