from django.urls import path
from account.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', account_page, name="account-page"),
    path('signup/', AccountCreateAPI.as_view(), name="signup"),
    path('signin/', LoginView.as_view(), name="signin"),
]
