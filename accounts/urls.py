from .views import *
from django.urls import path

urlpatterns = [
    path('', LoginView.as_view(), name='Login_Api'),
    path('signUp/', SignUpView.as_view(), name='SignUp_Api'),

]
