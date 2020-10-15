from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import HttpResponse
import oauth2
from django.template import loader
from django.views.generic import TemplateView

class ProductList(APIView):

    def get(request):
        model = Products.objects.all()
        serializer = ProductsSerializer(model,many=True)
        return Response(serializer.data)

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token= Token.objects.get_or_create(user=user)
        return Response(token.key)

class ProductList(APIView):

    def get(self,request):
        model = Products.objects.all()
        serializer = ProductsSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):

    def get_user(self, Model_No):
        try:
            model = Products.objects.get(id = Model_No)
            return model
        except Products.DoesNotExist:
            return

    def get(self,request, Model_No):
        if not self.get_user(Model_No):
            return Response(f'User with {Model_No} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsSerializer(self.get_user(Model_No))
        return Response(serializer.data)

    def put(self, request, Model_No):
        if not self.get_user(Model_No):
            return Response(f'User with {Model_No} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsSerializer(self.get_user(Model_No), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Model_No):
        if not self.get_user(Model_No):
            return Response(f'User with {Model_No} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(Model_No)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
