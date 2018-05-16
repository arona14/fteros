from rest_framework import serializers, exceptions
from django.conf import settings
from django.contrib.auth.models import Group
from crm.models import *

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError


# Get the UserModel
UserModel = get_user_model()

class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = [
            'id',
            'name'
            ]


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'interface_id'
            ]

class ExceptionAirlineSerializer(serializers.ModelSerializer):
    aircode = serializers.ReadOnlyField(source = 'airline.interface_id')
    class Meta:
        model = ExceptionAirline
        fields = [
            'id',
            'airline',
            'markup',
            'aircode',
            'net_value',
            'pub_value',
            'com_value'
            ]

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class MarkupReadSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only = True)
    x_airlines = ExceptionAirlineSerializer(source="exceptionairline_set", many = True, read_only = True)

    class Meta:
        model = Markup
        fields = '__all__'


class MarkupPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Markup
        fields = '__all__'

class RewardReadSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only = True)

    class Meta:
        model = Reward
        fields = '__all__'

class RewardPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = '__all__'

class DropnetReadSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only = True)

    class Meta:
        model = Dropnet
        fields = '__all__'
class DropnetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dropnet
        fields = '__all__'

class CustomerWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class CustomerReadSerializer(serializers.ModelSerializer):
    group = AffiliateSerializer(read_only = True)
    class Meta:
        model = Customer
        fields = [
            'id',
            'agency_id',
            'interface_id',
            'name',
            'address1',
            'address2',
            'city',
            'state',
            'country',
            'zip_code',
            'customer_type',
            'email',
            'phone',
            'fax',
            'group'
        ]

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'customer',
            'role',
            'logo',
            'affiliate',
            'is_active'
            ]

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):

    customer = CustomerReadSerializer(read_only = True)
    role = RoleSerializer( read_only = True)
    class Meta:
        model = User
        fields = '__all__'

class UserPasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'password'
            ]
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

class UserPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class UserListSerializer(serializers.ModelSerializer):
    role = RoleSerializer( read_only = True)
    customer = CustomerReadSerializer(read_only = True)
    affiliate = AffiliateSerializer(read_only = True)
    #logo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'is_active',
            'is_staff',
            'updated_by',
            'queue1',
            'queue2',
            'queue3',
            'queue4',
            'queue5',
            'customer',
            'role',
            'affiliate'
            ]


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name'
            ]

        
class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = '__all__'


class PccSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pcc
        fields = '__all__'



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
                user = self._validate_email(email, password)

            # Authentication through username
            elif app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password)

            # Authentication through either username or email
            else:
                user = self._validate_username_email(username, email, password)

        else:
            # Authentication without using allauth
            try:
                username = UserModel.objects.get(email__iexact=email).get_username()
            except UserModel.DoesNotExist:
                pass

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs


class UserCustomerListPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCustomerList
        fields = '__all__'

class UserCustomerListReadSerializer(serializers.ModelSerializer):
    customer = CustomerReadSerializer(read_only = True)
    user = UserListSerializer(read_only = True)
    class Meta:
        model = UserCustomerList
        fields = '__all__'
class CustomersAffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'interface_id'
            ]

class UsersCustomerAffiliateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class IdUserCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'interface_id'
            ]


