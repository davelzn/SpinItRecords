from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from django.shortcuts import redirect 

urlpatterns = [
    path('', lambda request: redirect('/prodotti/')),
    path('admin/', admin.site.urls),
    path('prodotti/', include("prodotti.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
