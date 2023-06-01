from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InvoiceDataSerializer
from .models import InvoiceData

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello, World!'})


# API views to use the serializers to serialize the data.
# Return the serialized data in the API response
@api_view(['GET'])
def invoice_data_list(request):
    invoices = InvoiceData.objects.all()
    serializer = InvoiceDataSerializer(invoices, many=True)
    return Response(serializer.data)