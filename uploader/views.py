from django.shortcuts import render
from django.http import JsonResponse
import os
from .models import FileUpload
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import * 
from datetime import datetime


def index(request):
    return render(request, 'upload.html')

def file_uploaded(request):
    return render(request, 'uploaded_files.html')

class FileUploadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        file_upload = FileUpload.objects.filter(auther=request.user)
        serializer = FileUploadSerializer(file_upload, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("this is post method ")
        print(request.data)
        try: 
            file = request.data.get('file').read()
            file_name =  str(datetime.now()).replace(" ", "-").replace(":", "-")   + "_" +  request.data.get('filename') 
            path =  settings.MEDIA_ROOT + '/users/' + file_name
            print(path, "path")
            with open(path, 'wb+') as destination: 
                destination.write(file)
            print(file_name, "file_name")
            file_upload = FileUpload(file_name = request.data.get('filename') , auther = request.user, upload = f"users/{file_name}")
            file_upload.save()
            return Response({'data':'Uploaded Successfully','existingPath': file_name})
        except:
            return Response({'data' : "file upload problem"}, status=status.HTTP_400_BAD_REQUEST)
