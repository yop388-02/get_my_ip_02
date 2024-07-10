import socket
import requests
from django.shortcuts import render

def get_client_name(first_name, last_name):
    nom = first_name
    prenoms = last_name
    return nom, prenoms


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def show_ip_addresses(request):

    private_ip = get_client_ip(request)

    # Obtenir l'adresse IP publique du visiteur
    try:
        public_ip = requests.get('https://api64.ipify.org').text
    except requests.RequestException:
        public_ip = 'Non disponible'

    nom, prenoms = get_client_name("Mon_Nom", "Mon_prénom")

    return render(request, 'show_ips.html', {"nom" : nom, 'prenoms' : prenoms, 'private_ip': private_ip, 'public_ip': public_ip})
