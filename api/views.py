from django.http import JsonResponse
from main.models import Members, Bills


def get_members(request):
    members = Members.objects.all()[0:60]
    data = {'members': list(members.values())}
    return JsonResponse(data)


def get_bills(request):
    bills = Bills.objects.all()[0:40]
    data = {'bills': list(bills.values())}
    return JsonResponse(data)
