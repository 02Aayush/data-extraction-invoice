from rest_framework import serializers
from .models import InvoiceData


#Serializers are used to convert complex data types (such as Django models) into JSON, XML, or other content types that
# can be easily rendered into API responses

class InvoiceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceData
        fields = '__all__'