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



class TimeTableAddView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = TimeTableSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response({'msg':'TimeTable Add Successful', "data":serializer.data}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    timetable = TimeTable.objects.all()
    serializer = TimeTableListSerializer(timetable, many=True)
    course = Course.objects.all()
    courseSerializer = CourseSerializer(course, many=True)
    subject = Subject.objects.all()
    subjectSerializer = SubjectSerializer(subject, many=True)
    return Response({"data":serializer.data, "courseList":courseSerializer.data, "subjectList":subjectSerializer.data}, status=status.HTTP_200_OK)
  

class TimeTableRetrieveUpdateDeleteAPIView(APIView):
    """Retrieve, update or delete a transformer instance 
    """
    def get_object(self, pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            return TimeTable.objects.get(pk=pk) 
        except TimeTable.DoesNotExist: 
            raise Http404 
  
    def get(self, request, pk, format=None): 
        timetable = self.get_object(pk) 
        serializer = TimeTableListSerializer(timetable) 
        return Response({"data":serializer.data}) 
  
    def put(self, request, pk, format=None):
        print('time table update', request.data) 
        timetable = self.get_object(pk) 
        serializer = TimeTableRetrieveUpdateDeleteSerializer(timetable, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"TimeTable Updated Successfully"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
  
    def patch(self, request, pk, format=None): 
        timetable = self.get_object(pk) 
        serializer = MarksheetRetrieveUpdateDeleteSerializer(timetable, 
                                           data=request.data, 
                                           partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"TimeTable Partially Updated"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None): 
        timetable = self.get_object(pk) 
        timetable.delete() 
        return Response({"msg":"TimeTable Deleted Successfully"},status=status.HTTP_204_NO_CONTENT) 