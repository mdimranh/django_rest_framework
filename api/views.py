from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer

from django.views.decorators.csrf import csrf_exempt

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
	# return JsonResponse(serializer.data)


# Query set all student data
def student_list(request):
	stu = Student.objects.all()
	serializer = StudentSerializer(stu, many = True)
	# print(serializer)
	# print(serializer.data)
	json_data = JSONRenderer().render(serializer.data)
	# print(json_data)
	return HttpResponse(json_data, content_type = 'application/json')
	# return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def student_create(request):
	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data = pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data created'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type = 'application/json')
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data, content_type = 'application/json')
