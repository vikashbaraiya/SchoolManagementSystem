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



class StudentRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = FacultySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'data':serializer.data, 'msg':'Faculty Add Successful'}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    serializer = StudentProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  


class FacultyAddView(APIView):
  renderer_classes = [UserRenderer]

  def post(self, request, format=None):
    serializer = FacultySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'data':serializer.data, 'msg':'Faculty Add Successfully'}, status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    course = Course.objects.all()
    course_serializer = CourseSerializer(course, many=True)
    college = College.objects.all()
    college_serializer = CollegeSerializer(college, many=True)
    subject = Subject.objects.all()
    subject_serializer = SubjectSerializer(subject, many=True) 
    faculty = Faculty.objects.all()
    serializer = FacultyListSerializer(faculty, many=True)
    return Response({"data":serializer.data, "courseList":course_serializer.data, "subjectList":subject_serializer.data, "collegeList":college_serializer.data}, status=status.HTTP_200_OK)
  

class FacultyRetrieveUpdateDeleteAPIView(APIView):
    """Retrieve, update or delete a Faculty instance 
    """
    def get_object(self, pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            return Faculty.objects.get(pk=pk) 
        except Faculty.DoesNotExist: 
            raise Http404 
  
    def get(self, request, pk, format=None): 
        faculty = self.get_object(pk) 
        serializer = FacultyListSerializer(faculty) 
        return Response({"data":serializer.data}) 
  
    def put(self, request, pk, format=None): 
        faculty = self.get_object(pk) 
        serializer = FacultyRetrieveUpdateDeleteSerializer(faculty, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Faculty Updated Successfully"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
  
    def patch(self, request, pk, format=None): 
        faculty = self.get_object(pk) 
        serializer = FacultyRetrieveUpdateDeleteSerializer(faculty, 
                                           data=request.data, 
                                           partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"data":serializer.data, "msg":"Faculty Partially Updated"}) 
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
          
  
    def delete(self, request, pk, format=None): 
        faculty = self.get_object(pk) 
        faculty.delete() 
        return Response({"msg":"Faculty Deleted Successfully"},status=status.HTTP_204_NO_CONTENT) 