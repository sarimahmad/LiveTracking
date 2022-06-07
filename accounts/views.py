
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


class SignUpView(APIView):
    serializers_class = SignUpSerializer

    def post(self, request):
        serializers = self.serializers_class(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            refresh = RefreshToken.for_user(user)
            data = serializers.data
            responce_data = {
                'access_token': str(refresh.access_token),
                'user': data
            }

            return Response(responce_data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = CustomerUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        data = GetUserSerializer(user)
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        responce_data = {
            'access_token': str(access_token),
            'user': data.data
        }
        return Response(responce_data, status=status.HTTP_200_OK)