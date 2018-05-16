#coding: utf-8
from gds.reservation import *
import pandas as pd
from crm.models import Customer
from gds.pnr import Pnr
import psycopg2

connexion = psycopg2.connect("host=165.227.213.58 dbname=backoffice user=postgres password=88Islam19")

def cityName(city_code):
    try:
   
        oriCountry = """ SELECT * FROM trams_countries WHERE airport_code = '{}' """.format(city_code[-3:])
        dfOriCountry = pd.read_sql(sql=oriCountry, con=connexion)
        firstCountry = str(dfOriCountry.iloc[0]['city_name'])
    
        return firstCountry
    except:
        return None
    
  

class Itinerarie(object):
        
    def getItinerary(self,pnr):
            
        data=Pnr().display_pnr(pnr)
        date_format = "%Y-%m-%d %H:%M"
        all_itinerary = []
        itinerary_dict = {}
        passenger_list = []
        try:
                
            status_list = Itinerary().segment_status_list(data)
            
            miles  = Itinerary().airlineflow(data)
            miles_all = 0
            new_value = 0
            if miles == None or len(miles) == 0:
                miles_all =0
            else:
                for i in miles:
                    miles_all = miles_all+int(i)
            if status_list != [] and status_list != None:
                
                for i in range(0, len(status_list)):
                    init = {}
                    airline = Itinerary().airline_list(data)
                    if airline == None or len(airline) == 0:
                        init['airline'] = ''
                    else:
                        init['airline'] = airline[i]
                    airline_name = Itinerary().airline_name(data)
                    if airline_name == None or len(airline_name) == 0:
                        init['airline_name'] = ''
                    else:
                        init['airline_name'] = airline_name[i]
                    init['from_code'] = Itinerary().origin_city_list(data)[i]
                    from_name = cityName(Itinerary().origin_city_list(data)[i])
                    if from_name != None:
                        init['from_name'] = from_name
                    else:
                        init['from_name'] = ""
                    init['to_code'] = Itinerary().destination_city_list(data)[i]
                    to_name = cityName(Itinerary().destination_city_list(data)[i])
                    if to_name != None:
                        init['to_name'] = to_name
                    else:
                        init['to_name'] = ""
                    
                    init['depart'] = Itinerary().departure_datetime_list(data)[i]
                    init['arrive'] = Itinerary().arrival_datetime_list(data)[i]
                    try:
                        if (Itinerary().destination_city_list(data)[i]) == (Itinerary().origin_city_list(data)[i+1]):
                            depart_year = Itinerary().departure_datetime_list(data)[i][0:4]
                            depart = Itinerary().departure_datetime_list(data)[i+1]
                            arrivee = (depart_year+'-'+Itinerary().arrival_datetime_list(data)[i]).replace('T',' ')
                            a = datetime.strptime(depart, date_format)
                            b = datetime.strptime(arrivee, date_format)
                            delta = a - b
                            if delta >= pd.Timedelta('2.5 days'):
                                init['stops'] = "Nonstop"
                            else:
                                init['stops'] = str(delta)
                        else:
                            init['stops'] = 'Nonstop'
                    except:
                        init['stops'] = 'Nonstop'
                    miles  = Itinerary().airlineflow(data)
                    if miles == None or len(miles) == 0:
                        init['miles'] = '0/0'
                    else:
                        
                        new_value = new_value+miles[i]
                        init['miles'] = str(new_value)+'/'+str(miles_all)
                    

                    if status_list[i]=='HK':
                        init['status'] = "CONFIRMED"
                    elif status_list[i] == "HX":
                        init['status'] = "CANCEL CONFIRM"
                    elif status_list[i] == "HL":
                        init['status'] = "HOLDS WAITLIST"
                    elif status_list[i] == "HX":
                        init['status'] = "HOLDING CONFIRMED"
                    elif status_list[i] == "UN":
                        init['status'] = "UNABLE "
                    elif status_list[i] == "EK":
                        init['status'] = "EMD CONFIRMED "
                    elif status_list[i] == "GF":
                        init['status'] = "FIRM BOOKING "
                    elif status_list[i] == "GN":
                        init['status'] = "GROUP BOOKING "
                    elif status_list[i] == "TK":
                        init['status'] = "Sched"
                    elif status_list[i] == "SS":
                        init['status'] = "Sell segment"
                    elif status_list[i] == "SQ":
                        init['status'] = "Space reques"
                    else:
                        init['status'] = status_list[i]
                    class_of_service =  Itinerary().class_of_service_list(data)
                    if class_of_service == None or len(class_of_service) == 0:
                        init['clss_of_service'] = ""
                    else:
                        init['clss_of_service'] = class_of_service[i]
                    flight_number_values = Itinerary().flight_number_list(data)
                    if flight_number_values == None or len(flight_number_values) == 0:
                        init['flight_number'] = ""
                    else:
                        init['flight_number'] = flight_number_values[i]
                    equipement_values = Itinerary().equipmentList(data)
                    if equipement_values == None or len(equipement_values)==0:
                        init['equipement'] = ""
                    else:
                        init['equipement'] = equipement_values[i]
                        
                    duration = Itinerary().flight_duration_list(data)
                    if duration == None or len(duration)== 0:
                        init['duration'] = ''
                    else:
                        init['duration'] = duration[i][0:2]+'h'+duration[i][3:5]+'m'
                    all_itinerary.append(init)
                itinerary_dict['segments'] = all_itinerary

                firstname = Passengers().first_name_list(data)

                for i in range(0, len(firstname)):
                    passenger = {}
                    
                    passenger['first_name'] = firstname[i]
                    passenger['last_name'] =  Passengers().surname_list(data)[i]
                    ticket_number =  Ticketing().ticketed_number_list(data)
                    if ticket_number == None or len(ticket_number) == 0:
                        passenger['ticket_number'] =  ''
                    else:
                        passenger['ticket_number'] =  ticket_number[i]
                    passenger_list.append(passenger)
                itinerary_dict['passengers'] = passenger_list
                issued_date = Ticketing().issue_date(data)
                if issued_date == None or len(issued_date) == 0 :
                    itinerary_dict['issued_date'] = ''
                else:
                    itinerary_dict['issued_date'] = Ticketing().issue_date(data)[0]

                base_amount = Pricing().base_fare_list(data)
                if base_amount==None or len(base_amount)==0:
                    itinerary_dict['base_amount'] = "0.00"
                else:
                    itinerary_dict['base_amount'] = base_amount[0]

                total_fare = Pricing().total_fare_list(data)
                if total_fare == None or len(total_fare)==0:
                    itinerary_dict['total_fare'] = "0.00"
                else:
                    itinerary_dict['total_fare'] = total_fare[0]

                tax = Pricing().total_tax_list(data)
                if tax == None or len(tax)==0:
                    itinerary_dict['tax'] = "0.00"
                else:
                    itinerary_dict['tax'] = tax[0]
                
                total_amount = Accounting().total_amount_list(data)
                if total_amount == None or len(total_amount) == 0:
                    itinerary_dict['total_amount'] = ""
                else:
                    itinerary_dict['total_amount'] = total_amount[0]
                    
                    
                itinerary_dict['pnr'] = pnr

                tax_value = Accounting().taxValue(data)
                tax_code = Accounting().taxCode(data)
                interface_id = Agency().agency_dk(data)
                customer_value =  Customer.objects.filter(interface_id=interface_id).values()
                if customer_value == None or  len(customer_value)==0:
                    itinerary_dict['customer_name'] = ""
                else:
                    customer = {}
                    customer['agency_id'] = customer_value[0].get("agency_id")
                    customer['interface_id'] = customer_value[0].get("interface_id")
                    customer['name'] = customer_value[0].get("name")
                
                    itinerary_dict['customer_name'] = customer
                if tax_code == None or len(tax_code) == 0:
                    itinerary_dict['XT_Tax'] = ""
                else:
                    if tax_code[0] == 'XT':
                        itinerary_dict['XT_Tax'] = tax_value[0]
                    else:
                        itinerary_dict['XT_Tax'] = ""
                    
                    if tax_code[0] == 'US':
                        itinerary_dict['US_Tax'] = tax_value[0]
                    else:
                        itinerary_dict['US_Tax'] = ""
                return  itinerary_dict
            else:
                return []
        except:
            return 2
                
