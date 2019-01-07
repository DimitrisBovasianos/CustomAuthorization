from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import MyUser
#from .serialiazers import ItemSerializer,CategoriesSerializer,UserSerializer,LoginSerializer,AddressSerializer,Delivery_InfoSerializer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponseRedirect,HttpResponse
import decimal
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from rest_framework import generics, permissions, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.core.cache import cache
import uuid
from django.http import HttpResponse
from django.core import serializers
import base64
from urllib import parse
from urllib import request as requestalter
import json
from .auth import MyAuthentication,MyAuthenticationRest


# Create your views here.
def Login(request):
    if request.method == 'POST':
        #if not request.POST.get('remember_me'):
            #request.session.set_expiry(0)
        username  = request.POST.get('username')
        password = request.POST.get('password')
        backend1 = MyAuthentication()
        user = MyUser.objects.get(username=username)
        user = backend1.authenticate(request,username,password)
        if user:
            login(request,user)

            return redirect('home')
        else:
            return HttpResponse(status=401)
    else:
        return render(request,'login.html')


def valid(request):
    return render(request,'home.html')

class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        return Response()
