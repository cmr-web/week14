from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Students


@api_view(['GET'])
def getUsers(request):
    model = Students.objects.all()
    serilazer = StudentSerializer(model, many=True)
    return Response(serilazer.data)


@api_view(['POST'])
def addUsers(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def searchUser(request):
    user = request.data.get('rollno')
    User = Students.objects.filter(rollno = user)
    serilazer = StudentSerializer(User, many=True)
    return Response(serilazer.data)

