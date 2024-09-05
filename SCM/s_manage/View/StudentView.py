from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from s_manage.models import User
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from s_manage.serializers import *

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class StudentRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    fixed_user_type_id = 2  # Set the fixed foreign key ID here
    user_type_instance = Group.objects.get(pk=fixed_user_type_id)

    data = request.data
    data['user_type'] = user_type_instance.pk
    serializer = StudentRegistrationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    serializer = StudentProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  


class StudentAddView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = StudentAddSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'data':serializer.data, 'msg':'Student Add Successfully'}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    college = College.objects.all()
    college_serializer = CollegeListSerializer(college, many=True)
    students = Student.objects.select_related('college_ID').all()
    serializer = StudentListSerializer(students, many=True)
    return Response({"data":serializer.data, 'preload_data':college_serializer.data})
  



class StudentRetrieveUpdateDeleteAPIView(APIView):
    """Retrieve, update or delete a transformer instance 
    """
    def get_object(self, pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            return Student.objects.get(pk=pk) 
        except Student.DoesNotExist: 
            raise Http404 
  
    def get(self, request, pk, format=None): 
        student = self.get_object(pk) 
        serializer = StudentListSerializer(student) 
        return Response({"data":serializer.data}) 
  
    def put(self, request, pk, format=None): 
        user = self.get_object(pk) 
        serializer = StudentRetrieveUpdateDeleteSerializer(user, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Student Updated Successfully"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
  
    def patch(self, request, pk, format=None): 
        student = self.get_object(pk) 
        serializer = StudentRetrieveUpdateDeleteSerializer(student, 
                                           data=request.data, 
                                           partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Student Partially Updated"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
          
  
    def delete(self, request, pk, format=None): 
        student = self.get_object(pk) 
        student.delete() 
        return Response({"msg":"Student Deleted Successfully"},status=status.HTTP_204_NO_CONTENT) 