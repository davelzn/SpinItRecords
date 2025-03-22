from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Prodotto(models.Model):
    nome = models.CharField(max_length = 50)
    descrizione = models.CharField(max_length = 5000)
    categoria = models.CharField(max_length = 80)
    immagine = models.ImageField()

# ForeignKey
class Preferito(models.Model):
    id_utente = models.ForeignKey(User, on_delete = models.CASCADE)
    id_prodotto = models.ForeignKey(Prodotto, on_delete =models.CASCADE)