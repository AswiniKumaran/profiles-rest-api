from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api.serializers import HelloSerializer,UserProfileSerializer
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

class HelloApiView(APIView):
    serializer_class=HelloSerializer
    def get(self,request,format=None):
        apiview=[
        "uses HTTP methods",
        "most control over logic",
        "mapped manually to urls",
        "similar to django functions"
        ]
        return Response({'message':"successful",'apiview':apiview})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello{name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request):
        return Response({'method':'PUT'})
    def patch(self,request):
        return Response({'method':'PATCH'})
    def delete(self,request):
        return Response({'method':'DELETE'})

class HelloAPiViewSet(viewsets.ViewSet):
    serializer_class=HelloSerializer
    def list(self,request):
        messge=[
            'automatically mapped to urls through routers',
            'involves less code change',
            'contains methods create,retreive,update,delete,partial_update'
        ]
        return Response({'messge':messge})
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'messge':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retreive(self,request):
        return Response({'method':'GET'})
    def update(self,request,pk=None):
        return Response({'method':'PUT'})
    def partial_update(self,request,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})

class UserProfileSerializer(viewsets.ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')
