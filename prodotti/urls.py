from django.urls import path
from .views import home, prodotti,dettaglio, recensioni, preferiti, login, register
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', home, name = "home"),    
    path('home/', home, name = "home"),
    path( '<int:id>/', dettaglio, name= "dettaglio"),
    path('recensioni/', recensioni, name='recensioni'),
    path('preferiti/', preferiti, name="preferiti"),
    path('prodotti/', prodotti, name="prodotti"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)