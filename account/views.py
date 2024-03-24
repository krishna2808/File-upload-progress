from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# from . import CustomAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import send_otp_email
import random
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def account_page(request):
    return render(request, "account/account.html")



class AccountCreateAPI(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AccountSerializer

class LoginView(TokenObtainPairView):

    pass

