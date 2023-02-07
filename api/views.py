from django.http import JsonResponse
from main.models import Members, Bills


def get_members(request):
    members = Members.objects.all()
    data = {'members': list(members.values())}
    return JsonResponse(data)


def search_members(request, query):
    members = Members.objects.all()
    if query is not None:
        if len(query) <= 2 and not query.isdigit():
            members = members.filter(state__iexact=query)
        else:
            members = members.filter(full_name__icontains=query)
    data = {'members': list(members.values())}
    return JsonResponse(data)


def get_bills(request):
    bills = Bills.objects.all()
    data = {'bills': list(bills.values())}
    return JsonResponse(data)


def search_bills(request, query):
    bills = Bills.objects.all()
    if query is not None:
        bills = bills.filter(title__icontains=query)
    data = {'bills': list(bills.values())}
    return JsonResponse(data)
