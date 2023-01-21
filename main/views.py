from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import BillSerializer, CreateBillSerializer
from .models import Bill
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class BillListView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class CreateBillView(APIView):
    serializer_class = CreateBillSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            date = serializer.data.get('date')
            summary = serializer.data.get('summary')
            vote = Bill(name=name, date=date, summary=summary)
            vote.save()
            return Response(BillSerializer(vote).data, status=status.HTTP_201_CREATED)


