from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method="post", request_body=StudentSerializer())
@api_view(['GET', 'POST'])
def home(request):

    if request.method == "GET":
        all_students = Student.objects.all()
        serializer = StudentSerializer(all_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response({"message":"successful", "data":serializer.data}, status=status.HTTP_201_CREATED)
        
        else:
            return Response({"message":"failed",
                             "error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)