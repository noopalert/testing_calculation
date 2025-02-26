from .models import *

from rest_framework import serializers

class ContractClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractClient
        fields = '__all__'

class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = '__all__'