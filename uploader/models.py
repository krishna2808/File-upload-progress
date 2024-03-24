from django.db import models
from account.models import User
# Create your models here.
class FileUpload(models.Model):
    auther = models.ForeignKey(User, related_name="file_auther", on_delete=models.CASCADE)
    upload = models.FileField(upload_to='users/')
    file_name = models.CharField(max_length=225, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_datetime',)
    