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



class CourseAddView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = CourseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response({'msg':'Course Add Successful', "data":serializer.data}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    course = Course.objects.all()
    serializer = CourseListSerializer(course, many=True)
    return Response({"data":serializer.data}, status=status.HTTP_200_OK)
  

class CourseRetrieveUpdateDeleteAPIView(APIView):
    """Retrieve, update or delete a transformer instance 
    """
    def get_object(self, pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            return Course.objects.get(pk=pk) 
        except Course.DoesNotExist: 
            raise Http404 
  
    def get(self, request, pk, format=None): 
        course = self.get_object(pk) 
        serializer = CourseListSerializer(course) 
        return Response({"data":serializer.data}) 
  
    def put(self, request, pk, format=None): 
        course = self.get_object(pk) 
        serializer = CourseRetrieveUpdateDeleteSerializer(course, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Course Updated Successfully"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
  
    def patch(self, request, pk, format=None): 
        course = self.get_object(pk) 
        serializer = CourseRetrieveUpdateDeleteSerializer(course, 
                                           data=request.data, 
                                           partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Course Partially Updated"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
          
  
    def delete(self, request, pk, format=None): 
        course = self.get_object(pk) 
        course.delete() 
        return Response({"msg":"Course Deleted Successfully"},status=status.HTTP_204_NO_CONTENT) 