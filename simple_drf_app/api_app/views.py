from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *

@api_view(['GET'])
def hello_world(request):
    return Response(data={"message": "Hello, world!"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def installment_calculation(request):
    if request.method == 'POST':
        id_contract_number = request.data.get('id')
        range_date = request.data.get('range_date')

        if not id_contract_number or not range_date:
            return Response({"error": "id and range_date are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            contract = ContractClient.objects.get(id=id_contract_number)
            otr = contract.otr
            dp = otr * 0.2
        
            pokok_utang = otr - dp

            if range_date <= 12:
                bunga = 0.12
            elif range_date > 12 and range_date <= 24:
                bunga = 0.14
            elif range_date > 24:
                bunga = 0.165

            total_payment = pokok_utang + (pokok_utang * bunga)
            installment = total_payment / range_date

            return Response({
                "installment": installment,
            }, status=status.HTTP_200_OK)
        except ContractClient.DoesNotExist:
            return Response({"error": "Contract number not found"}, status=status.HTTP_404_NOT_FOUND)

