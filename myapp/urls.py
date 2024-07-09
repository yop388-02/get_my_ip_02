from django.urls import path
from .views import show_ip_addresses

urlpatterns = [
    path('show_ips/', show_ip_addresses, name='show_ips'),
]
