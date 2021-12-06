from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

import json
# Model object - single student data

def student_detail(request, pk):
	stu = Student.objects.get(id = pk)
	# print(stu)
	serializer = StudentSerializer(stu)
	# print(serializer)
	# print(serializer.data)
	json_data = JSONRenderer().render(serializer.data)
	# json_data = json.dumps(serializer.data)
	# print(json_data)
	return HttpResponse(json_data, content_type = 'application/json')


# Query set all student data
def student_list(request):
	stu = Student.objects.all()
	serializer = StudentSerializer(stu, many = True)
	# print(serializer)
	# print(serializer.data)
	json_data = JSONRenderer().render(serializer.data)
	# print(json_data)
	return HttpResponse(json_data, content_type = 'application/json')