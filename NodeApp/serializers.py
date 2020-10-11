from rest_framework import serializers
from NodeApp.models import Products

class ProductsSerializer(serializers.ModelSerializer):

    Model_No = serializers.CharField(required=False)
    Name = serializers.CharField(required=False)
    Description = serializers.CharField(required=False)
    RAM = serializers.IntegerField(required=False)
    Processor = serializers.CharField(required=False)
    Type = serializers.CharField(required=False)
    class Meta:
        model = Products
        # fields = ('Name', 'Model_No')
        fields = '__all__'