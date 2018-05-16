from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

from gds.api.views import *

urlpatterns = [
    url( r'^schedchange/$', SchedChangeAPIView.as_view(), name='sched_chance' ),
    url( r'^passengers/$', PassengerAPIView.as_view(), name='list-passenger' ),
    url( r'^reservations/$', ReservationAPIView.as_view(), name='list-reservation' ),
    url( r'^detailschedchange/$', SegmentAPIView.as_view(), name='details' ),
    url(r'^sendemail/$', SendEmailAPIView.as_view(), name='email'),
    url(r'^travel/$', TravelAPIView.as_view(), name='travel'),
    url(r'^travelers/$', CustomerPassengerView.as_view(), name='Customer Passenger'),
    url(r'^senditinerary/$', SendItineraryAPIView.as_view(), name='itinerary'),
]


