from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView, GroupApiView
from account.views import *
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('group/', GroupApiView.as_view(), name="group" ),
    path('userlist/', UserRegistrationView.as_view(), name='userlist'),
    path('user/retrive/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user_retrive'),
    path('user/update/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user_update'),
    path('user/partial_update/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user_partial_update'),
    path('user/delete/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user_delete'),   
]