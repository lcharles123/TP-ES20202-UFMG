from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Direciona do root para a view de login 
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='dashboard/', permanent=True)),
]


