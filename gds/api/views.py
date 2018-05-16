from django.db.models import Q
from rest_framework import generics, mixins
from gds.api.serializers import *
from gds.models import *
from crm.models import Customer
from gds.request.detail import Mail
from gds.request.itinerary import  Itinerarie
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


# this view allow only read methods
class SchedChangeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pnr'
    serializer_class = SchedChangeSerializer

    def get_queryset(self):
        
        qs = []
        
        # ------ Getting querystrings if exists ----------
        query = self.request.GET.get("dk")

        aff = self.request.GET.get("aff")

        if aff is not None:
            cus = Customer.objects.filter(group=aff)
            dks = []
            
            for c in cus:
                dks.append(c.interface_id)

            qs = SchedChange.objects.filter(dk__in=dks)
            return qs  

        if query is not None:
            dks = str(query).split(',')
            qs = SchedChange.objects.filter(dk__in=dks)

        return qs
        


    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs)


class PassengerAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PassengerSerializer

    def get_queryset(self):
        return Passenger.objects.all()
    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)


class ReservationAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'pnr'
    serializer_class = ReservationSerializer

    def get_queryset(self):
        qs = Reservation.objects.filter(is_ticketed=False)

        query = self.request.GET.get("dk")

        aff = self.request.GET.get("aff")

        if aff is not None:
            cus = Customer.objects.filter(group=aff)
            dks = []

            for c in cus:
                dks.append(c.interface_id)

            qs = qs.filter(Q(interface_id__in=dks)).distinct()
            return qs      

        if query is not None:
            dks = str(query).split(',')
            qs = qs.filter(Q(interface_id__in=dks)).distinct()

        return qs

    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)

class SegmentAPIView(generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = SegmentSchedChangeSerializer

    def get_queryset(self):
        qs = SegmentSched.objects.all()

        pnr = self.request.GET.get("pnr")

        if pnr is not None:      
            qs = qs.filter(Q(pnr = pnr)).distinct()   

        return qs

class SendEmailAPIView(APIView):
    serializer_class = SendEmailSerializer
    
    def get(self, request, format=None):

        pnr = request.query_params.get('pnr', None)
        email = request.query_params.get('email', None)
        if pnr is not None and email is not None:
            obj = Mail().sendMail(email,pnr)
            print(obj)
            resul = 'Done'
        else:
            resul = 'Failed'
        return Response(resul)

class TravelAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TravelSerializer

    def get_queryset(self):
        qs = Travel.objects.all() 
        return qs

    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)

class CustomerPassengerView(generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = PassengerSerializer

    def get_queryset(self):
        dk = self.request.GET.get('dk')
        dks = str(dk).split(',')
        qs = Passenger.objects.filter(travel__pnr__interface_id__in=dks)
        return qs


class SendItineraryAPIView(APIView):
    def get(self, request, format=None):

        pnr = request.query_params.get('pnr', None)
        if pnr is not None:
            resul = Itinerarie().getItinerary(pnr)
        else:
            resul = 'The pnr is required'
        return Response(resul)