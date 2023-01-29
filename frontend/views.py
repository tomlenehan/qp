from django.http import JsonResponse
from django.shortcuts import render
from main.models import Bills
from main.models import Members


def index(request, *args, **kwargs):

    all_bills = Bills.objects.all()[:20]
    all_members = Members.objects.all()[:20]
    context = {
        'bills': all_bills,
        'members': all_members
    }
    return render(request, 'frontend/index.html')




