from django.contrib import admin
from .models import Prodotto, Valutazione, Commento
# Register your models here.
admin.site.register(Prodotto)
admin.site.register(Valutazione)
admin.site.register(Commento)

