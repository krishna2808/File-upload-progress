from rest_framework import serializers
from .models import * 


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['auther', 'upload', "file_name"]