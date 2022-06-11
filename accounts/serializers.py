from rest_framework import serializers
from .models import *
from django.utils.translation import gettext_lazy as _

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=5, write_only=True, required=True)


    class Meta:
        model = CustomerUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user


class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField(error_messages={'null': 'This feild cannot be nulll'})
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = CustomerUser.objects.get(email=email)
            except Exception as e:
                msg = _('User Does not Exit')
                raise serializers.ValidationError(msg, code='authorization')

            if not user.check_password(password):
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')


        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        data['user'] = user
        return data



