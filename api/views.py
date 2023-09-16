from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header

from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import UserSerializer
from .models import User

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email = request.data['email']).first()

        if not user:
            raise APIException('Invalid Credentials')
        
        if not user.check_password(request.data['password']):
            raise APIException('Invalid Credentials')
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key = 'refreshToken', value = refresh_token, httponly = True)
        response.data = {
            'token' : access_token
        }

        return response
    
class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.filter(pk = id).first()

            return Response(UserSerializer(user).data)
        
        raise AuthenticationFailed('Unauthenticated')
    
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token' : access_token
        })
    
class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key = "refreshToken")
        response.data = {
            'message': "SUCCESS"
        }
        return response
    
class ToDoAPIView(APIView):

    def get(self, request, pk=None, format =None):
        try:
            if pk:
                Todo_obj = ToDo.objects.get(pk = pk)
                serializer = ToDoSerializer(Todo_obj)
        except Exception as e:
            return HttpResponseRedirect("/")
        else:
            items = ToDo.objects.all()
            serializer = ToDoSerializer(items, many = True)
        return Response(serializer.data)
    
    #create
    def post(self, request, format=None):
        data = request.data
        serializer = ToDoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #update
    def put(self, request, pk, format=None):
        Todo_obj = ToDo.objects.get(pk = pk)
        serializer = ToDoSerializer(data = request.data, instance = Todo_obj)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message" : "Data Updated Successfully"})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    #partial update
    def patch(self, request, pk, format=None):
        Todo_obj = ToDo.objects.get(pk = pk)
        serializer = ToDoSerializer(data = request.data, instance = Todo_obj, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message" : "Data Updated Successfully"})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=True):
        ToDo.objects.get(pk=pk).delete()
        return Response({"Message" : "Data Deleted Successfully"})