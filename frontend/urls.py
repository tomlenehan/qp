from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('bills', index),
    path('members', index),
]
