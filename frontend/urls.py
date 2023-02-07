from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('bills', index),
    path('bills/<str:query>/', index),
    path('members', index),
    path('members/<str:query>/', index),
]
