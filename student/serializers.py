from rest_framework import serializers
from .models import Student, ProfileUpload

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'department', 'term', 'level', 'student_id', 'admission']

# class ProfileUploadSerializer():