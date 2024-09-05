from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import User
from .models import *
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util

"""Serializer User as a Student Form"""
class StudentRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

  class Meta:
    model = User
    fields=['email', 'username', 'first_name', 'last_name', 'dob', 'address', 'gender', 'mobilenumber', 'password', 'password2', 'user_type']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)
  

"""Serialize Student Profile Form"""
class StudentProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'first_name', 'last_name', 'dob', 'user_type', 'address', 'gender', 'mobilenumber']


"""Serialize College Form"""
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
      model = College
      fields = ['collegeName', 'collegeAddress', 'collegeCity', 'collegeState', 'collegePhoneNumber']

    def create(self, validate_data):
      return College.objects.create(**validate_data)
    

"""Serialze Course Form"""
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
      model = Course
      fields = ['courseName', 'courseDuration', 'courseDescription']

    def create(self, validate_data):
      return Course.objects.create(**validate_data)
    

"""Serialize Marksheet Form"""
class MarkSheetSerializer(serializers.ModelSerializer):
    class Meta:
      model = Marksheet
      fields = ['rollNumber', 'name', 'physics', 'chemistry', 'maths']

    def create(self, validate_data):
      return Marksheet.objects.create(**validate_data)
    
"""Serialize Student Form"""
class StudentAddSerializer(serializers.ModelSerializer):
    class Meta:
      model = Student
      fields = ['firstName', 'lastName', 'dob', 'email', 'mobileNumber', 'college_ID']

    def create(self, validate_data):
      return Student.objects.create(**validate_data)
    
"""Serialize Subject"""
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
      model = Subject
      fields = ['subjectName', 'subjectDescription', 'course_ID']

    def create(self, validate_data):
      return Subject.objects.create(**validate_data)
    
"""Serialize Faculty Form"""
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
      model = Faculty
      fields = ['firstName', 'lastName', 'email', 'password', 'address', 'gender', 'dob', 'college_ID', 'course_ID', 'subject_ID']

    def create(self, validate_data):
      return Faculty.objects.create(**validate_data)
    
"""Serialize TimeTable Form"""
class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
      model = TimeTable
      fields = ['examTime', 'examDate', 'subject_ID', 'course_ID', 'semester']

    def create(self, validate_data):
      return TimeTable.objects.create(**validate_data)
    



class StudentListSerializer(serializers.ModelSerializer):
  college_ID = CollegeSerializer()
  class Meta:
    model = Student
    fields = ['id','firstName', 'lastName', 'dob', 'email', 'mobileNumber', 'college_ID']

class StudentRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):

  class Meta:
    model = Student
    fields=['firstName', 'lastName', 'dob', 'email', 'mobileNumber','college_ID']
    

  def create(self, validate_data):
    return Student.objects.create(**validate_data)
  


class CollegeListSerializer(serializers.ModelSerializer):
  class Meta:
    model = College
    fields = ['id','collegeName', 'collegeAddress', 'collegeState', 'collegeCity', 'collegePhoneNumber']




class CollegeRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):

  class Meta:
    model = College
    fields=['collegeName','collegeCity', 'collegeAddress', 'collegePhoneNumber','collegeState']
    

  def create(self, validate_data):
    return College.objects.create(**validate_data)
  


class CourseListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['id','courseName', 'courseDescription', 'courseDuration']


class CourseRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):

  class Meta:
    model = Course
    fields=['courseName', 'courseDescription', 'courseDuration']



class FacultyListSerializer(serializers.ModelSerializer):
  college_ID = CollegeSerializer()
  course_ID = CourseSerializer()
  subject_ID = SubjectSerializer()
  class Meta:
    model = Faculty
    fields = ['id','firstName', 'lastName', 'email', 'address', 'gender', 'dob', 'college_ID', 'subject_ID', 'course_ID']


class FacultyRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):

  class Meta:
    model = Faculty
    fields=['firstName', 'lastName', 'email', 'address', 'gender', 'dob', 'college_ID', 'subject_ID', 'course_ID']
    

  def create(self, validate_data):
    return Faculty.objects.create(**validate_data)
  



class SubjectListSerializer(serializers.ModelSerializer):
  course_ID = CourseSerializer()
  class Meta:
    model = Subject
    fields = ['id','subjectName', 'subjectDescription', 'course_ID']


class SubjectRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):

  class Meta:
    model = Subject
    fields=['subjectName', 'subjectDescription', 'course_ID']

  def create(self, validate_data):
    return Subject.objects.create(**validate_data)




class MarksheetListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marksheet
    fields = ['id','rollNumber', 'name', 'physics', 'chemistry', 'maths']


class MarksheetRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):

  class Meta:
    model = Marksheet
    fields=['rollNumber', 'name', 'physics', 'chemistry', 'maths']

  def create(self, validate_data):
    return Marksheet.objects.create(**validate_data)
  

class TimeTableListSerializer(serializers.ModelSerializer):
  subject_ID = SubjectSerializer()
  course_ID = CourseSerializer()
  class Meta:
    model = TimeTable
    fields = ['id','examTime', 'examDate', 'subject_ID', 'course_ID', 'semester']


class TimeTableRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    subject_ID = SubjectSerializer()
    course_ID = CourseSerializer()

    class Meta:
        model = TimeTable
        fields = ['id', 'examTime', 'examDate', 'subject_ID', 'course_ID', 'semester']

    def create(self, validated_data):
        subject_data = validated_data.pop('subject_ID')
        course_data = validated_data.pop('course_ID')

        course, created = Course.objects.get_or_create(**course_data)
        subject, created = Subject.objects.get_or_create(course=course, **subject_data)

        timetable = TimeTable.objects.create(subject=subject, course=course, **validated_data)
        return timetable

    def update(self, instance, validated_data):
        subject_data = validated_data.pop('subject_ID')
        course_data = validated_data.pop('course_ID')

        course, created = Course.objects.get_or_create(**course_data)
        subject, created = Subject.objects.get_or_create(course_ID=course, **subject_data)

        instance.examTime = validated_data.get('examTime', instance.examTime)
        instance.examDate = validated_data.get('examDate', instance.examDate)
        instance.subject = subject
        instance.course = course
        instance.semester = validated_data.get('semester', instance.semester)
        instance.save()
        return instance
    