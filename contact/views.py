from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ContactSerializer

from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import JSONParser

from .models import Contact

class ContactApi(APIView):
    def get(self, request, format = None):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

