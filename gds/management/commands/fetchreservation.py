from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from gds.models import Reservation, Passenger, Travel, SchedChange
from gds.pnr import Pnr, token
from gds.reservation import *

class GDSReservation(object):

    def __init__(self, object_xml):
        self._object_xml = object_xml
		
    def getReservation(self):

        status_list = Itinerary().segment_status_list(self._object_xml)

        if status_list != [] and status_list != None:
            res = Reservation()

            res.interface_id = Agency().agency_dk(self._object_xml)
            if res.interface_id == None:
                res.interface_id = None
            origin = Itinerary().origin_city_list(self._object_xml)
            if len(origin) == 0 or origin == None:
                res.origin = None
            else:
                res.origin = origin[0]
            destination = Itinerary().destination_city_list(self._object_xml)
            if len(destination) == 0 or destination == None:
                res.destination = None
            else:
                res.destination = ",".join(destination)

            departure_date = Itinerary().departure_datetime_list(self._object_xml)
            if len(departure_date) == 0 or departure_date == None:
                res.departure_date = None
            else:
                res.departure_date = departure_date[0]

            res.return_date = None

            carriers = Itinerary().carrier_list(self._object_xml)
            if len(carriers) == 0 or carriers == None:
                res.carriers = None
            else:
                res.carriers = ",".join(carriers)

            validating_carrier = Itinerary().validating_carrier_list(self._object_xml)
            if len(validating_carrier) == 0 or validating_carrier == None:
                res.validating_carrier = None
            else:
                res.validating_carrier = validating_carrier[0]

            class_of_service = Itinerary().class_of_service_list(self._object_xml)
            res.class_of_service = ",".join(class_of_service)

            res.payement_card = Pricing().payement_card(self._object_xml)
            if res.payement_card == None:
                res.payement_card = None

            res.ticketing_pcc = Ticketing().ticketing_pcc(self._object_xml)
            if res.ticketing_pcc == None:
                res.ticketing_pcc = None

            res.ticketing_agent = Ticketing().ticketing_agent(self._object_xml)
            if res.ticketing_agent == None:
                res.ticketing_agent = None

            res.frequent_flyer = Itinerary().frequent_flyer(self._object_xml)
            if res.frequent_flyer == None:
                res.frequent_flyer = None

            res.booking_pcc = Itinerary().bookingPcc(self._object_xml)
            if res.booking_pcc == None:
                res.booking_pcc = None

            res.booking_agent = Itinerary().bookingAgent(self._object_xml)
            if res.booking_agent == None:
                res.booking_agent = None

            res.is_ticketed = Ticketing().is_ticketed(self._object_xml)
            airline = Itinerary().airline_list(self._object_xml)
            res.airline = ",".join(airline)


            return res
        
        else:
            return None

    def passengers(self):
        
       
        list_firstname = Passengers().first_name_list(self._object_xml)	
        if len(list_firstname)==0 or list_firstname ==None:
            pass
        else:
            list_lastname = Passengers().surname_list(self._object_xml)
            if list_lastname == None:
                list_lastname =[]
            if len(list_lastname)>len(list_firstname):
                l =0
                while len(list_lastname)!= len(list_firstname):
                    del list_lastname[-1]
                    l = l+1
            elif len(list_lastname)<len(list_firstname):
                l = 0
                while len(list_lastname)!=len(list_firstname):
                    list_lastname.append('')
                    l=l+1
            list_passenger_type = Passengers().passenger_type_list(self._object_xml)

            if list_passenger_type==None:
                list_passenger_type=[]

            if len(list_passenger_type)>len(list_firstname):
                p =0
                while len(list_passenger_type)!= len(list_firstname):
                    del list_passenger_type[-1]
                    p = p+1
            
            elif len(list_passenger_type)<len(list_firstname):
                p =0
                while len(list_passenger_type)!= len(list_firstname):
                    list_passenger_type.append('')
                    p = p+1
            
            list_birthdate = Passengers().date_of_birth_list(self._object_xml)
            if list_birthdate== None or len(list_birthdate)==0:
                list_birthdate=[]

            if len(list_birthdate)>0:
                new_birthday_list = []
                for i in list_birthdate:
                    if i in new_birthday_list:
                        pass
                    else:
                        new_birthday_list.append(i)
                list_birthdate=new_birthday_list
                
            if len(list_birthdate)>len(list_firstname):
                b = 0
                while len(list_birthdate)!=len(list_firstname):
                    del list_birthdate[-1]
                    b=b+1
            elif len(list_birthdate)<len(list_firstname):
                b = 0
                while len(list_birthdate)!=len(list_firstname):
                    list_birthdate.append('0001-01-01')
                    b=b+1
            list_tkt_number = Ticketing().ticketed_number_list(self._object_xml)
            if list_tkt_number == None:
                list_tkt_number=[]
            if len(list_tkt_number)>len(list_firstname):
                t = 0
                while len(list_tkt_number)!=len(list_firstname):
                    del list_tkt_number[-1]
                    t=t+1
            
            elif len(list_tkt_number)<len(list_firstname):
                t = 0
                while len(list_tkt_number)!=len(list_firstname):
                    list_tkt_number.append('')
                    t =t+1
            
            list_tkt_issu_date = Ticketing().issue_date(self._object_xml)
            if list_tkt_issu_date ==  None:
                list_tkt_issu_date = []
            elif len(list_tkt_issu_date)>len(list_firstname):
                tk = 0
                while len(list_tkt_issu_date)!=len(list_firstname):
                    del list_tkt_issu_date[-1]
                    tk=tk+1
            elif len(list_tkt_issu_date)<len(list_firstname):
                tk = 0
                while len(list_tkt_issu_date)!=len(list_firstname):
                    list_tkt_issu_date.append('')
                    tk =tk+1
            l_passenger = []

            for i in range(0, len(list_firstname)):
                data_passenger= {}

                data_passenger['firstname'] = list_firstname[i]
                data_passenger['lastname'] = list_lastname[i]
                data_passenger['passenger_type'] = list_passenger_type[i]
                data_passenger['birthdate'] = list_birthdate[i]
                data_passenger['tkt_number'] = list_tkt_number[i]
                data_passenger['ticketing_issu_date'] = list_tkt_issu_date[i]
                l_passenger.append(data_passenger)
                
            return l_passenger


class Command(BaseCommand):
    help = 'Fetch the reservations in Q68 - Custom commannd'

    def handle(self, *args, **options):
        p = Pnr()
        q = 68

        list_pnr = p.list_of_pnr_in_q(q)
        command = 'QZAP/WR1768'
        p.send_sabre_entry(token,command)	

        for i in list_pnr:
            obj_xml = Pnr().display_pnr(i)
            reserObj = GDSReservation(obj_xml)
            aRes = reserObj.getReservation()
            if aRes is not None:
                aRes.pnr = i
                print(aRes.pnr,aRes.interface_id,aRes.booking_agent,aRes.booking_pcc,aRes.origin,aRes.destination,aRes.departure_date,aRes.return_date,aRes.carriers,aRes.validating_carrier,aRes.class_of_service,aRes.payement_card,aRes.ticketing_pcc,aRes.ticketing_agent,aRes.frequent_flyer,aRes.is_ticketed)
                try:
                    aRes.save()
                    print('Reservation is saved')
                    sch =  SchedChange.objects.filter(pnr__iexact=i)
                    if sch is not None:
                        status_list = Itinerary().segment_status_list(obj_xml)
                        s = 0
                        for k in status_list:
                            if k != 'HK':
                                s = s+1
                        if s == 0:
                            sch.delete()
                            print('sch deleted')
                    if aRes.is_ticketed == True:
                        
                        
                        p_list = reserObj.passengers()
                        for item in p_list:
                            p_object = Passenger()
                            p_object.firstname = item['firstname']
                            p_object.lastname = item['lastname']
                            p_object.passenger_type = item['passenger_type']
                            p_object.birthdate = item['birthdate']
                            p_object.save()
                            print('Passenger is saved')
                            t_object = Travel()
                            t_object.pnr = aRes
                            t_object.passenger = p_object
                            t_object.tkt_number =  item['tkt_number']
                            t_object.ticketing_issu_date =  item['ticketing_issu_date']
                            t_object.save()
                            print('Travel is saved')
                except:
                    print('Something goes wrong')
            else:
                res = Reservation.objects.filter(pnr__iexact=i)
                print('Reservation with status list vide or N/A')
                #print(res)
                if res is not None:
                    res.delete()
                    print('reservation deleted')
                sch =  SchedChange.objects.filter(pnr__iexact=i)
                if sch is not None:
                    sch.delete()
                    print('sch deleted')