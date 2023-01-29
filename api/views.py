from django.http import JsonResponse
from django.shortcuts import render
from main.models import Members, Bills


def get_members(request):
    members = Members.objects.all()
    data = {'members': list(members.values())}
    return JsonResponse(data)


def get_bills(request):
    bills = Bills.objects.all()
    data = {'bills': list(bills.values())}
    return JsonResponse(data)
