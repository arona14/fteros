from django.core.management.base import BaseCommand, CommandError
from gds.models import SchedChange, SegmentSched
from gds.pnr import Pnr, token
from gds.reservation import *
from datetime import datetime

def toDate(d_list):
    l = []
    for i in d_list:
        l.append(datetime.strptime(i, "%Y-%m-%d %H:%M"))
    return l

def toDateArrival(d_list):
    today = datetime.today()
    y = str(today.year)
    l = []
    for i in d_list:
        l.append(datetime.strptime(y+'-'+i, "%Y-%m-%dT%H:%M"))
    return l
class ScheduleChange(object):

    def __init__(self, object_xml):
        self._object_xml = object_xml

    def getChange(self):

        #sched_change = {}
        status_list = Itinerary().segment_status_list(self._object_xml)

        if status_list != []:
            for j in status_list:
                if j != 'HK':
                    ch = SchedChange()
                    ch.status = j
                    ch.dk = Agency().agency_dk(self._object_xml)
                    ch.cc_agent = Ticketing().ticketing_agent(self._object_xml)
                    ch.t_pcc = Ticketing().ticketing_pcc(self._object_xml)
                    
                    pax_names = Passengers().full_name_list(self._object_xml)
                    pax_names  = " , ".join(pax_names)
                    
                    ch.pax_names = pax_names
                    ch.is_ticket = Ticketing().is_ticketed(self._object_xml)
                    ch.booking_pcc = Itinerary().bookingPcc(self._object_xml)
                    ch.booking_agent = Itinerary().bookingAgent(self._object_xml)
                    list_departure_dates1 = Itinerary().departure_datetime_list(self._object_xml)
                    departure = toDate(list_departure_dates1)
                    ch.departure_date=departure[0]
                    return ch
            
            return None
        
        else:
            return None

    def getDetails(self):
        list_airlines = Itinerary().airline_list(self._object_xml)
        list_fligth_nos = Itinerary().flight_number_list(self._object_xml)
        list_origins = Itinerary().origin_city_list(self._object_xml)
        list_destinations = Itinerary().destination_city_list(self._object_xml)
        list_departure_dates1 = Itinerary().departure_datetime_list(self._object_xml)
        list_departure_dates = toDate(list_departure_dates1)
        list_arrivals_dates1 = Itinerary().arrival_datetime_list(self._object_xml)
        list_arrivals_dates = toDateArrival(list_arrivals_dates1)
        list_status = Itinerary().segment_status_list(self._object_xml)

        l_segSchChange = []

        for i in range(0, len(list_airlines)):
            segSch = SegmentSched()

            segSch.airline = list_airlines[i]
            segSch.fligthno = list_fligth_nos[i]
            segSch.origin = list_origins[i]
            segSch.destination = list_destinations[i]
            segSch.departure_date = list_departure_dates[i]
            segSch.arrival_date = list_arrivals_dates[i]
            segSch.status = list_status[i]

            l_segSchChange.append(segSch)

        return l_segSchChange

class Command(BaseCommand):
    help = 'Fetch the schedule changes in Q70 - Custom commannd'

    def handle(self, *args, **options):
        p = Pnr()
        q = 70

        list_pnr = p.list_of_pnr_in_q(q)

        for i in list_pnr:
            obj_xml = Pnr().display_pnr(i)
            schChng = ScheduleChange(obj_xml)
            sch = schChng.getChange()

            if sch is not None:
                sch.pnr = i
                #try:
                sch.save()
                print('schedule change insert success')

                oldDetails = SegmentSched.objects.filter(pnr = sch.pnr)

                if(len(oldDetails)):
                    for old in oldDetails:
                        old.delete()

                schSegList = schChng.getDetails()
                for item in schSegList:
                    item.pnr = sch
                    item.save()

                #except:
                #    print('Something goes wrong with this pnr')

            else:
                print('pnr without more infos or status OK - PASS')
                    