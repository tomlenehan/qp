from django.urls import path
from .views import get_members
from .views import get_bills

urlpatterns = [
    path('get_members/', get_members, name='members'),
    path('get_bills/', get_bills, name='members'),
]