from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Prodotto(models.Model):
    nome = models.CharField(max_length = 50)
    descrizione = models.CharField(max_length = 5000)
    categoria = models.CharField(max_length = 80)
    immagine = models.ImageField()
    artista = models.CharField(max_length = 100)
    anno_uscita = models.CharField(max_length = 5)
    link_streaming = models.CharField(max_length = 5000)
    etichetta = models.CharField(max_length = 100)
    nazione = models.CharField(max_length=100, null=True, blank=True)
    lingua = models.CharField(max_length=50, null=True, blank=True)

# ForeignKey
class Preferito(models.Model):
    id_utente = models.ForeignKey(User, on_delete = models.CASCADE)
    id_prodotto = models.ForeignKey(Prodotto, on_delete =models.CASCADE)


class Valutazione(models.Model):
    id_utente = models.ForeignKey(User, on_delete = models.CASCADE)
    id_prodotto = models.ForeignKey(Prodotto, on_delete =models.CASCADE)
    punteggio = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

class Commento(models.Model):
    id_utente = models.ForeignKey(User, on_delete = models.CASCADE)
    id_prodotto = models.ForeignKey(Prodotto, on_delete =models.CASCADE)
    testo = models.CharField(max_length=5000) 
    data = models.DateTimeField(auto_now_add=True)  