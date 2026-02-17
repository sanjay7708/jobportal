
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from . serializers import SignupSerializer
# Create your views here.
class LoginView(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        if not username or not password:
            return Response({'message':'username or password required'},status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(request,username=username,password=password) 
        if not user:
            return Response({'message':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

        refresh=RefreshToken.for_user(user)
        return Response({'message':'login sucessfully','access':str(refresh.access_token),'refresh':str(refresh)},status=status.HTTP_200_OK)


class SignupView(APIView):
    def post(self,request):
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Register Sucessfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    def post(self,request):
        refresh_token=request.data.get('refresh')
        if not refresh_token:
             return Response({'message':'refresh token must required'},status=status.HTTP_400_BAD_REQUEST)
        try:
            token=RefreshToken(refresh_token)
            token.blacklist()
        except:
            pass
        return Response({"message":"logout sucessfull"},status=status.HTTP_205_RESET_CONTENT)