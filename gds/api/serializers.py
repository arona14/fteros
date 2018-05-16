from rest_framework import serializers

from gds.models import *

class SchedChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedChange
        fields = '__all__'


class SegmentSchedChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegmentSched
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many = True, read_only = True)
    
    class Meta:
        model = Reservation
        fields = '__all__'



class SendEmailSerializer(serializers.Serializer):
    pnr = serializers.CharField(max_length=100)
    email  = serializers.CharField(max_length=100)

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

