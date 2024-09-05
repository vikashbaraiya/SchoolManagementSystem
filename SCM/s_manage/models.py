from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username,user_type, first_name, last_name, dob,address, gender, mobilenumber, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            dob = dob,
            user_type = user_type,
            address = address,
            gender = gender,
            mobilenumber = mobilenumber
        )
        

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username,user_type, email, first_name, last_name, dob, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
            dob = dob,
            user_type = user_type
        )

        user.is_admin = True,
        user.is_staff = True,
        user.is_superuser = True,
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobilenumber = models.CharField(max_length=11)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.ForeignKey(Group, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'dob', 'user_type']

    objects = CustomUserManager()

    def __str__(self):
        return self.username + ',' + self.email
    

class College(models.Model):
    collegeName = models.CharField(max_length=50)
    collegeAddress = models.CharField(max_length=50)
    collegeState = models.CharField(max_length=50)
    collegeCity = models.CharField(max_length=50)
    collegePhoneNumber = models.CharField(max_length=10)

    class Meta:
        db_table = 'SCM_COLLEGE'


class Course(models.Model):
    courseName = models.CharField(max_length=50)
    courseDescription = models.CharField(max_length=100)
    courseDuration = models.CharField(max_length=100)

    class Meta:
        db_table = 'SCM_COURSE'



class Marksheet(models.Model):
    rollNumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()

    class Meta:
        db_table = 'SCM_MARKSHEET'


class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    mobileNumber = models.CharField(max_length=20)
    email = models.EmailField()
    college_ID = models.ForeignKey(College, on_delete=models.CASCADE)


    class Meta:
        db_table = 'SCM_STUDENT'


class Subject(models.Model):
    subjectName = models.CharField(max_length=50)
    subjectDescription = models.CharField(max_length=50)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'SCM_SUBJECT'


class Faculty(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    college_ID = models.ForeignKey(College, on_delete=models.CASCADE)
    subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)


    class Meta:
        db_table = 'SCM_FACULTY'


class TimeTable(models.Model):
    examTime = models.CharField(max_length=40)
    examDate = models.DateField()
    subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)

    class Meta:
        db_table = 'SCM_TIMETABLE'

