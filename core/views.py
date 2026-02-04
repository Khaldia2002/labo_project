from django.shortcuts import render

def accueil(request):
    return render(request, 'accueil.html')

def a_propos(request):
    return render(request, 'a_propos.html')

def equipes(request):
    return render(request, 'equipes.html')

def projets(request):
    return render(request, 'projets.html')

def publications(request):
    return render(request, 'publications.html')

def actualites(request):
    return render(request, 'actualites.html')

def contact(request):
    return render(request, 'contact.html')

def connexion(request):
    return render(request, 'connexion.html')
