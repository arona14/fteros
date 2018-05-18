from django.db.models import Q
from rest_framework import generics, mixins, status
from crm.api.serializers import *
from crm.models import Affiliate, Customer, Contract, Markup, Reward, Dropnet, ExceptionAirline, User, UserManager, Sign,Pcc,UserCustomerList,\
Groupe,CustomerGroup,CustomerMarkup,CustomerReward
from rest_framework.response import Response
from django.http import Http404

class AffiliateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = AffiliateSerializer

    def get_queryset(self):
        qs = Affiliate.objects.all()
        query = self.request.GET.get("name")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AffiliateRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = AffiliateSerializer

    def get_queryset(self):
        return Affiliate.objects.all()

class AirlineAPIView(generics.ListAPIView):
    serializer_class = AirlineSerializer

    def get_queryset(self):
        qs = Customer.objects.all().filter(
            Q(customer_type__iexact='V')
            ).distinct()
        return qs


class CustomerAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerWriteSerializer
        return CustomerReadSerializer
    def get_queryset(self):
        qs = Customer.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__istartswith = query)|
                Q(interface_id__istartswith = query)|
                Q(email__istartswith = query)|
                Q(phone__istartswith = query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = CustomerWriteSerializer

    def get_queryset(self):
        return Customer.objects.all()

class ExceptionAirlineAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = ExceptionAirlineSerializer

    def get_queryset(self):
        qs = ExceptionAirline.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ExceptionAirlineRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = ExceptionAirlineSerializer

    def get_queryset(self):
        return ExceptionAirline.objects.all()

class ContractAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractSerializer

    def get_queryset(self):
        qs = Contract.objects.all() 
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains = query)|
                Q(description__icontains = query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContractRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractSerializer

    def get_queryset(self):
        qs = Contract.objects.all()

        name = self.request.GET.get("name")
        
        if name is not None:
            qs = qs.filter(
                Q(contract__name__iexact = name)
                ).distinct()

        return qs



class MarkupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MarkupPostSerializer
        return MarkupReadSerializer

    def get_queryset(self):
        qs = Markup.objects.all() 
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MarkupRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = MarkupPostSerializer

    def get_queryset(self):
        return Markup.objects.all()

class CustomerMarkupAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerMarkupPostSerializer
        return CustomerMarkupReadSerializer

    def get_queryset(self):
        qs = CustomerMarkup.objects.all() 
        
        dk = self.request.GET.get("q")
        
        if dk is not None:
            qs = qs.filter(
                Q(customer__agency_id__iexact = dk) 
                ).distinct()

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class CustomerMarkupRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = CustomerMarkupPostSerializer

    def get_queryset(self):
        return CustomerMarkup.objects.all()
class RewardAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RewardPostSerializer
        return RewardReadSerializer

    def get_queryset(self):
        qs = Reward.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RewardRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = RewardPostSerializer

    def get_queryset(self):
        return Reward.objects.all()

class CustomerRewardAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerRewardPostSerializer
        return CustomerRewardReadSerializer

    def get_queryset(self):
        qs = CustomerReward.objects.all() 
        
        dk = self.request.GET.get("q")
        
        if dk is not None:
            qs = qs.filter(
                Q(customer__agency_id__iexact = dk) 
                ).distinct()

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class CustomerRewardRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = CustomerRewardReadSerializer

    def get_queryset(self):
        return CustomerReward.objects.all()
class DropnetAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DropnetPostSerializer
        return DropnetReadSerializer

    def get_queryset(self):
        qs = Dropnet.objects.all() 
        airline = self.request.GET.get("airline")
        if airline is not None:
            qs = qs.filter(
                Q(airline__iexact = airline)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DropnetRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = DropnetPostSerializer

    def get_queryset(self):
        return Dropnet.objects.all()

class UserCreateAPIView(generics.CreateAPIView):

    model = User
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serialized = UserCreateSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = UserListSerializer

    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get("email")
        agency_id = self.request.GET.get("agency_id")
        if query is not None:
            qs = qs.filter(
                Q(email__iexact=query)
                ).distinct()

        if agency_id is not None:
            qs = qs.filter(Q(customer__agency_id = agency_id))
        return qs


class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserDetailSerializer
        return UserUpdateSerializer

    def get_queryset(self):
        return User.objects.all()

class UserPasswordResetView(generics.UpdateAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')

    serializer_class = UserPasswordResetSerializer
    def get_queryset(self):
        return User.objects.all()

class UserUpdatePasswordView(generics.UpdateAPIView):
    serializer_class = UserPasswordUpdateSerializer
    model = User
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    
    serializer_class = CommunicationSerializer

    def get_queryset(self):
        qs = Communication.objects.all() # Getting all communication
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(agency__id__iexact=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommunicationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = CommunicationSerializer

    def get_queryset(self):
        return Communication.objects.all()

class SignAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SignSerializer
    def get_queryset(self):
        qs = Sign.objects.all()
        query = self.request.GET.get("user")
        if query is not None:
            u = int(query)
            qs = qs.filter(
                Q(user__id__iexact=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SignRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SignSerializer

    def get_queryset(self):
        return Sign.objects.all()

class PccAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PccSerializer

    def get_queryset(self):
        qs = Pcc.objects.all()
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PCcRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = PccSerializer

    def get_queryset(self):
        qs = Pcc.objects.all()
        return qs


class UserCustomerListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCustomerListPostSerializer
        return UserCustomerListReadSerializer

    def get_queryset(self):
        qs = UserCustomerList.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(user__id__iexact=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserCustomerListRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class =UserCustomerListPostSerializer

    def get_queryset(self):
        return UserCustomerList.objects.all()


class CustomersAffiliateView(generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = CustomersAffiliateSerializer

    def get_queryset(self):
        affiliate_value = self.request.GET.get('affiliate')

        if affiliate_value is not None:
            qs = Customer.objects.filter(group=affiliate_value)
        else:
            qs = []
            
        return qs

class UsersCustomerAffiliateView(generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = UsersCustomerAffiliateListSerializer

    def get_queryset(self):
        affiliate_value = self.request.GET.get('affiliate')

        if affiliate_value is not None:
            qs = User.objects.filter(customer__group=affiliate_value)
        else:
            qs = []

        return qs

class IdUserCustomerView(generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = IdUserCustomersSerializer

    def get_queryset(self):
        id_value = self.request.GET.get('userID')
        
        if id_value is not None:    
            qs = Customer.objects.filter(usercustomerlist__user=id_value)
        else:
            qs = []

        return qs

class GroupeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """Groupe list and post view class"""


    lookup_field = 'id' 
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GroupePostSerializer
        return GroupeReadSerializer
    def get_queryset(self):
        qs = Groupe.objects.all()
        query = self.request.GET.get("name")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GroupeRudView(generics.RetrieveUpdateDestroyAPIView):
    """Groupe Retrieve Update Destroy"""


    lookup_field = 'id'
    serializer_class = GroupePostSerializer

    def get_queryset(self):
        return Groupe.objects.all()

class CustomerGroupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """Customer Group API view class"""


    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerGroupPostSerializer
        return CustomerGroupReadSerializer

    def get_queryset(self):
        qs = CustomerGroup.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                #1Q(groupe__name__iexact=query)|
                Q(customer__id__iexact=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerGroupRudView(generics.RetrieveUpdateDestroyAPIView):
    """Customer Groupe Retrieve Update Destroy view class"""

    
    lookup_field = 'id' 
    serializer_class =CustomerGroupPostSerializer

    def get_queryset(self):
        return CustomerGroup.objects.all()