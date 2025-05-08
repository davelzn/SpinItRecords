from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from prodotti.models import Prodotto,Preferito

# Create your views here.
def home(request):
    if request.method=="GET":
        return render(request, "prodotti/home.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, "prodotti/login.html", {
                "logged": True,
                "user": user
            })
        else:
            messages.error(request, "Credenziali non valide")

    return render(request, "prodotti/login.html", {
        "logged": request.user.is_authenticated,
        "user": request.user
    })

    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username già esistente")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email già registrata")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registrazione avvenuta con successo!")
        return redirect("login") 

    return render(request, "prodotti/register.html")
    
def prodotti(request):
    if request.method=="GET":
        cata_prodotti = Prodotto.objects.all()
        context = {"cata_prodotti": cata_prodotti}
        return render(request, "prodotti/prodotti.html", context)

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
def recensioni(request):
    return render(request, 'prodotti/recensioni.html')

def preferiti(request):
    return render(request, 'prodotti/preferiti.html')

def set_cookie(request):
    response = HttpResponse('Impostare un cookie')
    response.set_cookie('user_prefernce', 'dark_mode', max_age=3600)
    return response
def get_cookie(request):
    preference = request.COOKIES.get('user_prefernce','default_mode')
    return HttpResponse(f'La prefernza é: {preference}')
def delete_cookie(request):
    response = HttpResponse('Cookie eliminato!')
    response.delete_cookie('user_preference')    
    return response

def user_status(request):
    return {
        "logged": request.user.is_authenticated,
        "user": request.user
    }
