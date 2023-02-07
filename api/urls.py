from django.urls import path
from .views import get_members, search_members, get_bills, search_bills

urlpatterns = [
    path('get_members/', get_members, name='members'),
    path('get_members/<str:query>/', search_members, name='members'),
    path('get_bills/', get_bills, name='bills'),
    path('get_bills/<str:query>/', search_bills, name='bills'),
]