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



class SubjectAddView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SubjectSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response({'msg':'Subject Add Successful', "data":serializer.data}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    course = Course.objects.all()
    courseserializer = CourseListSerializer(course, many=True)
    students = Subject.objects.select_related('course_ID').all()
    serializer = SubjectListSerializer(students, many=True)
    return Response({"data":serializer.data, 'preload_data':courseserializer.data})
  

class SubjectRetrieveUpdateDeleteAPIView(APIView):
    """Retrieve, update or delete a Subject instance 
    """
    def get_object(self, pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            return Subject.objects.get(pk=pk) 
        except Subject.DoesNotExist: 
            raise Http404 
  
    def get(self, request, pk, format=None): 
        subject = self.get_object(pk) 
        serializer = SubjectListSerializer(subject) 
        return Response({"data":serializer.data})  
  
    def put(self, request, pk, format=None): 
        subject = self.get_object(pk) 
        serializer = SubjectRetrieveUpdateDeleteSerializer(subject, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Subject Updated Successfully"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
  
    def patch(self, request, pk, format=None): 
        course = self.get_object(pk) 
        serializer = SubjectRetrieveUpdateDeleteSerializer(course, 
                                           data=request.data, 
                                           partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Subject Partially Updated"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
          
  
    def delete(self, request, pk, format=None): 
        subject = self.get_object(pk) 
        subject.delete() 
        return Response({"msg":"Subject Deleted Successfully"},status=status.HTTP_204_NO_CONTENT) 