"""gerenciadorIOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# Use include() to add URLS from the dashboard application and authentication system
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls)
]

# mapeia para os links no app dashboard em /dashboard/urls.py
'''
from dashboard import views
urlpatterns += [
path('dashboard', views.dashboard, name='signup') # signup contida no mesmo arquivo acima
]
'''
#adicionado a url para redirecionamento / -> dashboard



#aponta para arquvos estaticos de js, imagens e css
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Direciona do root para a view de login 
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    path('dashboard/', include('dashboard.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='dashboard/', permanent=True)),
]

'''
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import login
from gerenciadorIOT.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.login_redirect, name = 'login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account/$', core_views.account_page, name = 'account_page')

]'''



