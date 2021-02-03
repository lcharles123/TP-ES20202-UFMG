from django.urls import path
from dashboard import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.signup, name='signup'), # signup contida no mesmo arquivo acima
    path('', views.dashboard, name='dashboard') #quando / eh obtido referencia a classe dashboard contida em dashboard/views.py
    
]

# estao declaradas aqui todas as urls do site que apontam para a respectiva funcao no dashboard
urlpatterns += [
    path('links', views.links, name='links'),
    path('addlink', views.addlink, name='addlink'),
    path('removelink', views.removelink, name='removelink'),
	path('graficos', views.graficos, name='graficos'), 
	path('ajuda', views.ajuda, name='ajuda'), 
	path('conta', views.conta, name='conta'), 
    path('acoes', views.acoes, name='acoes'), 
    path('api', views.api, name='api'), 
    path('logout', views.logout, name='logout'), 
    
]

urlpatterns += [
    url(r'^password/$', views.conta, name='change_password'),
]









