from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file-upload/', views.FileUploadAPIView.as_view(), name='file-upload'),
    path('file-uploaded/', views.file_uploaded, name='file-uploaded'),
]