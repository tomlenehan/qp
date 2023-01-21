from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'name', 'date', 'summary')

class CreateBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('name', 'date', 'summary')
