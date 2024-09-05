from urllib import request
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from s_manage.models import User
from account.serializers import GroupSerializer, GroupViewSerializer
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from account.serializers import *
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from s_manage.pagination import CustomPagination

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  pagination_class = CustomPagination
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful',}, status=status.HTTP_201_CREATED)

  def get(self, request, format=None):
    group = Group.objects.all()
    group_serializer = GroupViewSerializer(group, many=True)

    user = User.objects.all()
    serializer = UserProfileSerializer(user, many=True)
    return Response({"data":serializer.data, "preload_data":group_serializer.data})

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    print("serializer : ",serializer)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    if not email or not password:
      return Response({'errors': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if user is not None:
      user_data = UserProfileSerializer(user).data
      print(user_data)
      token = get_tokens_for_user(user)
      headers = {
        'Cache-control': 'no-store, max-age=0',
        # ...
        'X-Frame-Options': 'DENY'
       }
      return Response({'token':token, 'msg':'Login Success', "data":user_data}, status=status.HTTP_200_OK, headers=headers)
    else:
      return Response({'errors':{'non_field_errors':'Email or Password is not Valid', }}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user = request.user
        if user.is_anonymous:
            return Response({'errors': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            return Response({'msg': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)


class GroupApiView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
      serializer = GroupSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"msg":"Group Add Successfully"}, status=status.HTTP_200_OK)

    def get(self,request, format=None):
        group = Group.objects.all()
        print("group:", group)
        serializer = GroupViewSerializer(group, many=True)
        return Response({"data":serializer.data})
    

class UserRetrieveUpdateDeleteAPIView(APIView):
    """Retrieve, update or delete a user instance 
    """
    def get_object(self, pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            return User.objects.get(pk=pk) 
        except User.DoesNotExist: 
            raise Http404 
  
    def get(self, request, pk, format=None): 
        user = self.get_object(pk) 
        serializer = UserProfileSerializer(user) 
        return Response({"data":serializer.data}) 
  
    def put(self, request, pk, format=None): 
        user = self.get_object(pk) 
        serializer = UserRetrieveUpdateDeleteSerializer(user, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"User Updated Successfully"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
  
    def patch(self, request, pk, format=None): 
        user = self.get_object(pk) 
        serializer = UserRetrieveUpdateDeleteSerializer(user, 
                                           data=request.data, 
                                           partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"User Partially Updated"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
          
  
    def delete(self, request, pk, format=None): 
        user = self.get_object(pk) 
        user.delete() 
        return Response({"msg":"User Deleted Successfully"},status=status.HTTP_204_NO_CONTENT) 