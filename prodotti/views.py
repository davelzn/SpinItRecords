from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from prodotti.models import Prodotto,Preferito

# Create your views here.
def home(request):
    if request.method=="GET":
        cata_prodotti = Prodotto.objects.all()
        context = {"cata_prodotti": cata_prodotti}
        return render(request, "prodotti/home.html", context)
    
def dettaglio(request, id):
    if request.method=="GET":
        prod = Prodotto.objects.get(id=id)
        context = {
                'prod': prod,
                "prod.nome": prod.nome,
                "prod.descrizione": prod.descrizione,
                "prod.categoria": prod.categoria,
                "prod.immagine": prod.immagine,
                "prod.artista" : prod.artista,
                "prod.anno_uscita" : prod.anno_uscita,
                "prod.link_streaming" : prod.link_streaming,
                "prod.etichetta" : prod.etichetta
                }
        return render(request, "prodotti/dettaglio.html", context)