from django.urls import path
from .views import home, prodotti, dettaglio, recensioni, login_view, register, logout_view, toggle_preferito, lista_preferiti
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('<int:id>/', dettaglio, name="dettaglio"),
    path('<int:prodotto_id>/recensioni/', recensioni, name='recensioni'),
    path('preferiti/', lista_preferiti, name='preferiti'),
    path('catalogo/', prodotti, name="prodotti"),
    path('login/', login_view, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name='logout'),
    path('preferiti/toggle/<int:id>/', toggle_preferito, name='toggle_preferito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
