from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import FileSerializer
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to File Upload API"})
# Create your views here.

class FileUploadedView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,status=201)
        return Response(file_serializer.errors,status=400)
    
       
