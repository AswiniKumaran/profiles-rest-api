from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self,request,format=None):
        apiview=[
        "uses HTTP methods",
        "most control over logic",
        "mapped manually to urls",
        "similar to django functions"
        ]
        return Response({'message':"successful",'apiview':apiview})
