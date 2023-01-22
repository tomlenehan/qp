from rest_framework import serializers
from .models import Bills


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('id', 'name', 'date', 'summary')


class CreateBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('name', 'date', 'summary')
