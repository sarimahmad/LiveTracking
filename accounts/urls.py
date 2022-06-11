from .views import *
from django.urls import path

urlpatterns = [
    path('', LoginView.as_view(), name='Login_Api'),
    path('signUp/', SignUpView.as_view(), name='SignUp_Api'),
    path('checkUser/', CheckUser.as_view(), name='Check_User_Api'),
    path('ChangePassword/', ChangePassword.as_view(), name='Change_Password_Api'),

]
