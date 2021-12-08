from django.urls import path
from .views import *

urlpatterns = [
    path('createstudent/', CreateStudentAPI.as_view()),
    path('stulist/', StudentListView.as_view()),
    path('studetails/<pk>', StudentDetailView.as_view()),
    path('getstudent/<str:department>', GetStudentList.as_view()),
]