from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView ,ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers, ProfileUpload

class CreateStudentAPI(APIView):
    def post(self, request, format = None):
        data = JSONParser().parse(request)
        serializer = StudentSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class = None

class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class GetStudentList(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'department'
    queryset = Student.objects.all()
    serializer_class = StudentSerializers