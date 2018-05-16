# -*- coding: utf-8 -*-
import pandas as pd
import jxmlease
import datetime
import re
from datetime import date, timedelta, datetime,time


####################################### Itinerary class ##################################
class Itinerary(object):

	
	def segment_status_list(self, data):
		""" Retrive a list wich contains all status codes
			for each segment """

		status_code = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				status = node.get_xml_attr('Status')
				status_code.append(str(status))
		except:
			status_code = None
	
		return status_code
	
	def airline_list(self, data):
		""" Retrieve a list which contains all airlines for each segment"""
		
		airlines = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				airline = node['tir38:MarketingAirline'].get_xml_attr('Code')
				airlines.append(str(airline))	
		except:
			airlines = None
	
		return airlines

	def airline_name(self, data):
    	
		""" Retrieve a list which contains all airlines for each segment"""
		
		name_airline = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				name_airline1 = node['tir38:MarketingAirline']['tir38:Banner']
				name_airline.append(str(name_airline1[11:]))	
		except:
			name_airline = None
	
		return name_airline
		
	def carrier_list(self, data):
		""" Retrieve a list which contains all airlines for each segment"""
		
		carriers = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				carrier = node['tir38:OperatingAirline'].get_xml_attr('Code')
				carriers.append(str(carrier))
		except:
			carriers = None
	
		return carriers

	def origin_city_list(self, data):
		""" Retrieve a list which contains origines
			city list for each segment """

		origin_locations = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				origin_location = node['tir38:OriginLocation'].get_xml_attr('LocationCode')
				origin_locations.append(str(origin_location))
		except:
			origin_locations = None

		return origin_locations 
	
	def airlineflow(self, data):
		airline_flow = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				airline_flow1 = node.get_xml_attr('AirMilesFlown')
				airline_flow.append(int(airline_flow1))
		except:
			airline_flow = None

		return airline_flow 

	
	

	def equipmentList(self, data):
		equipment = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				equipment1 = node['tir38:Equipment'].get_xml_attr('AirEquipType')
				equipment.append(str(equipment1))
		except:
			equipment = None

		return equipment 

	def destination_city_list(self, data) :
		""" Retrieve a list which contains destination city
			for each segment """ 

		destination_locations = []
		try:

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				destination_location = node['tir38:DestinationLocation'].get_xml_attr('LocationCode')
				destination_locations.append(str(destination_location))
	
		except:
			destination_locations = None
		
		return destination_locations

	def flight_number_list(self, data):
		""" This methode retrieve a list wich combers 
		of flight for each segment """

		flight_numbers = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				flight_number = node['tir38:OperatingAirline'].get_xml_attr('FlightNumber')
				flight_numbers.append(str(flight_number))
		except:
			flight_numbers = None
			
		return flight_numbers

	def class_of_service_list(self, data):
		""" This methode retrieve a list wich combers 
		of flight for each segment """

		class_of_services = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				class_of_service = node.get_xml_attr('ResBookDesigCode')
				class_of_services.append(str(class_of_service))
		except:
			class_of_services = None
			
		return class_of_services

	def flight_duration_list(self, data):
		""" This method retrieve a list which contains flight duration """

		duration_times = []
		try:
			
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				duration_time = node.get_xml_attr('ElapsedTime')
				duration_times.append(str(duration_time))
		except:
			duration_times = None
		return duration_times

	def departure_datetime_list(self, data):
		""" Return list wich contains departure datetime """


		departure_datetimes = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				departure_datetime = node.get_xml_attr('DepartureDateTime')
				departure_datetime = departure_datetime.replace('T',' ')
				departure_datetimes.append(str(departure_datetime))
		except:
			departure_datetimes = None
		return departure_datetimes

	def arrival_datetime_list(self, data):
		""" Retrieve list wich contains arrival datetimes """

		arrival_datetimes = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				arrival_datetime = node.get_xml_attr('ArrivalDateTime')
				arrival_datetimes.append(str(arrival_datetime))
		except:
			arrival_datetimes = None
		return arrival_datetimes
	
	def updated_depature_datetime_list(self, data):
		""" Retrieve list wich contains updated depature datetimes """

		update_datetimes = []

		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				update_datetime = node['tir38:UpdatedDepartureTime']
				update_datetimes.append(str(update_datetime))
		except:
			update_datetimes = None
		return update_datetimes

	def get_pnr(self, data):
		""" get the agency's dk """

		try:
			root = jxmlease.parse(data)
			pnr = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef'].get_xml_attr('ID')
		except:
			pnr = None
		return pnr
	
	def miscsegment_list(self, data):
		""" Retrieve list which contains all messages text
			from  MiscSegment """ 

		msg_list = []

		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ReservationItems/tir38:Item/tir38:MiscSegment/tir38:Text"):
				miscsegment = node
				msg_list.append(str(miscsegment))
			
		except:
			msg_list = None
		return msg_list
		
	def miscsegment_status_list(self, data):
		""" Retrieve list which contains all status
			from  MiscSegment """ 

		msg_status = []

		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ReservationItems/tir38:Item/tir38:MiscSegment"):
				msg = node.get_xml_attr('Status')
				msg_status.append(str(msg))
		except:
			msg_status = None
		return msg_status

	def validating_carrier_list(self, data):
		"""Return the validating carrier for this reservation"""

		validatingcarriers = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:PriceQuote/tir38:PricedItinerary"):
				validatingcarrier = node.get_xml_attr('ValidatingCarrier')
				validatingcarriers.append(str(validatingcarrier))
		except:
			validatingcarriers = None
		return validatingcarriers


	def frequent_flyer(self, data):
		""" get the return fidelity """

		try:
			root = jxmlease.parse(data)
			frequent = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:CustomerInfo']['tir38:CustLoyalty'].get_xml_attr('MembershipID')
		except:
			frequent = None
		return frequent

	def bookingPcc(self, data):
		
		try:
			root = jxmlease.parse(data)
			booking_pcc= root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('HomePseudoCityCode')
		except:
			booking_pcc = None
		return booking_pcc
	
	def bookingAgent(self, data):
		
		try:
			root = jxmlease.parse(data)
			booking_agent= root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('CreationAgent')
		except:
			booking_agent = None
		return booking_agent
	
################################### Passenger class ####################################

class Passengers(object):

	def first_name_list(self, data):
		""" Retrieve a list which contains all passengers firstname 
			for each segment """

		first_names= []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				
				first_name = node['tir38:GivenName']
				first_names.append(str(first_name))
		except:
			first_names = None
		return first_names
		

	def surname_list(self, data):
		""" Retrieve a list which contains all passengers surname 
			for each segment """

		surnames= []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				
				surname = node['tir38:Surname']
				surnames.append(str(surname))
		except:
			surnames = None
		return surnames	

	def full_name_list(self,data):
		""" Retrieve a list which contains all passengers fullname 
			for each segment """

		full_names = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				
				full_name=node['tir38:GivenName']+ ' '+node['tir38:Surname']
				full_names.append(str(full_name))
		except:
			full_names = None
		return full_names
	
	def passenger_type_list(self, data):
		""" this method contains list of all passenger type"""

		pass_types = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				pass_type = node.get_xml_attr('PassengerType')
				pass_types.append(str(pass_type))
		except:
			pass_type = None
		return pass_types

	def date_of_birth_list(self, data):
		""" this method retrieve the list of passengers's date of birth """

		birth_days = []

		try:
			
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				changed= node.get_xml_attr('SSR_Type',None) is not None
				if changed==False:
					pass
				elif changed==True:
					if node.get_xml_attr('SSR_Type') == "DOCS":
						bd = str(node['tir38:Text'])
						birth = re.search(r"[0-9]{2}[A-Z]{3}[0-9]+",bd,flags=0).group(0)
						day = birth[0:2]
						month = birth[2:5]
						year = birth[5:9]
						if month == 'JAN':
							month = '01'
						elif month == 'FEB':
							month = '02'
						elif month == 'MAR':
							month = '03'
						elif month == 'APR':
							month = '04'
						elif month == 'MAY':
							month = '05'
						elif month == 'JUN':
							month = '06'
						elif month == 'JUL':
							month = '07'
						elif month =='AUG':
							month = '08'
						elif month == 'SEP':
							month = '09'
						elif month == 'OCT':
							month = '10'
						elif month== 'NOV':
							month = '11'
						elif month =='DEC':
							month = '12'
						datetime_object = datetime.strptime(year+'-'+month+'-'+day,"%Y-%m-%d").strftime('%Y-%m-%d')

						birth_days.append(datetime_object)
		except:
			birth_days = None
		return birth_days
			
	def email_list(self, data):
		""" this method retrieve the list of passengers's date of birth """
		try:
			emails = []

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				if node.get_xml_attr('SSR_Type') == "CTCE":
					email1 = str(node['tir38:Text'])
					email2 = re.search(r'[\w\.-]+//[\w\.-]+',email1).group(0)
					email3 = email2.replace('//','@')
					emails.append(email3)
		except:
			emails = None
				
		return emails

	def phone_list(self, data):
		""" this method retrieve the list of passengers's phone """
		try:
			phones = []

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				value= node.get_xml_attr('SSR_Type',None) is not None
				if value==False:
					pass
				else:

					if node.get_xml_attr('SSR_Type') == "CTCM":
						phone1 = str(node['tir38:Text'])
						phone2 = re.search(r'[0-9]{5,}',phone1).group(0)
						phones.append(phone2)
						phones = list(set(phones))
		except:
			phones = None
				
		return phones

	def gender_list(self, data):
		""" this method allows to know the list of passenger's gender """

		g_list = []

		try:

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				if node.get_xml_attr('SSR_Type') == "DOCS":
					gender1 = str(node['tir38:Text'])
					gender2 = gender1.split('/')
					for i in gender2:
						if i=="F" or i=="M":
							gender=i
						g_list.append(gender)
					
		except:
			g_list = None
		return g_list

	
###################################### Agency class ######################################

class Agency(object):


	def agency_dk(self, data):
		""" get the agency's dk """

		try:
			root = jxmlease.parse(data)
			dk = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef'].get_xml_attr('CustomerIdentifier')
		except:
			dk = None
		return dk


	def agency_phone_list(self, data):
		""" retrieve the phone list of agency"""

		phones = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:ContactNumbers/tir38:ContactNumber"):
				phone1 = node.get_xml_attr("Phone")
				phones.append(str(phone1))
		except:
			phones = None
		return phones
	
	def agency_address(self, data):
		""" this method retrieve a list which contains agency addresses """

		addresslines = []
		try:
			for path, _, node in jxmlease.parse(data,generator="tir38:CustomerInfo/tir38:ContactNumbers/tir38:ContactNumber"):
				addressline1 = node.get_xml_attr('LocationCode')
				addresslines.append(str(addressline1))
		except:
			addresslines = None
		return addresslines

	def agency_name(self):

		name = []
		try:
			print(1)
		except:
			name = ['N/A']
		return name

	def agency_email(self):

		mail = []
		try:
			print(1)
		except:
			mail = ['N/A']
		return mail

	def agency_pcc(self, data):
		""" get the agency's pcc """

		try:
			root = jxmlease.parse(data)
			pcc = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('AAA_PseudoCityCode')
		except:
			pcc = None
		return pcc

	def agency_create(self, data):
		""" get the agency who create the reservation """

		try:
			root = jxmlease.parse(data)
			agent = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('CreationAgent')
		except:
			agent = None
		return agent

########################################### Pricing class #####################################

class Pricing(object):
	
	def  base_fare_list(self, data):
		"""This methed return price list for this reservation"""

		basefares = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				basefare1 = node['tir38:BaseFare'].get_xml_attr('Amount')
				basefares.append(str(basefare1))
		except:
			basefares = None
		return basefares

	def total_fare_list(self, data):
		""" this method retrieve a list which contains totals fares for this reservation  """

		totalfares = []
		try:
			 for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				 totalfare1 = node['tir38:TotalFare'].get_xml_attr('Amount')
				 totalfares.append(str(totalfare1))

		except:
			totalfares = None
		return totalfares
	
	def tax_detail(self):

		taxdetail = []
		try:
			print(1)
		except:
			taxdetail = ['N/A']
		return taxdetail
	
	def total_tax_list(self, data):
		""" Retrieve a list which contains total tax for this reservation """

		totaltax = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				totaltax1 = node['tir38:Totals']['tir38:Taxes']['tir38:Tax'].get_xml_attr('Amount')
				totaltax.append(totaltax1)
			
		except:
			totaltax = None
		return totaltax
	
	def pricing_type(self):

		type = []
		try:
			print(1)
		except:
			type = ['N/A']
		return type
	
	def payement_card(self, data):
		""" retrieve the phone list of agency"""

		try:
			root = jxmlease.parse(data)
			payement = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:AccountingInfo']['tir38:PaymentInfo']['tir38:Payment']['tir38:CC_Info']['tir38:PaymentCard'].get_xml_attr('Number')
		except:
			payement = None
		return payement

############################################ Rules class #################################################

class Rules():


	def baggage_allowance_list(self, data):
		""" Retrieve a list which contains baggage allowance """

		baggages = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ItineraryPricing/tir38:PriceQuote/tir38:PricedItinerary/tir38:AirItineraryPricingInfo/tir38:PTC_FareBreakdown/tir38:FlightSegment"):
				baggage1 = node['tir38:BaggageAllowance'].get_xml_attr("Number","")
				baggages.append(str(baggage1))
			baggages.remove('')
		except:
			baggages = None	
		return baggages

	def refund(self):

		refund_police = []
		 
			
		return refund_police

	def changed(self):

		changed = []
		 
			
		return changed

############################################# Ticketing class ########################################

class Ticketing():

	def is_ticketed(self, data):
		""" Return true if reservation is ticketed false else """
		ticket_number_list = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				ticket_number = node.get_xml_attr('eTicketNumber',"")
				ticket_number_list.append(str(ticket_number)) 
			if ticket_number_list == ['']:
				return False
			for i in ticket_number_list:
				try:
					p = re.search(r'(TE)[ ][0-9]+',i, flags=0).group()
				except:
					p = ""
				if len(p)>1:
					return True

		except:
			return False 
	
	def is_exchange_list(self, data):
		""" Return true if reservation is exchange false else """

		exchange_list = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:AccountingInfo/tir38:TicketingInfo/tir38:Exchange"):
				exchange = node.get_xml_attr('Ind')
				exchange_list.append(str(exchange))
		except:
			exchange_list = None
		return exchange_list
	
	def ticketed_number_list(self, data):
		""" Retrieve a list which contains ticket number """

		ticket_numbers = []
		ticket_number_list = []
		try:
		
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				ticket_number = node.get_xml_attr('eTicketNumber',"")
				ticket_number_list.append(str(ticket_number))
			for i in ticket_number_list:
				if i=='' or 'TV' in i or 'TK' in i : 
					pass
				else:
					
					tkt_number1 = re.search(r"(TE)[ ][0-9]+",i,flags=0).group(0)
					tkt_number2 = re.search(r'[0-9]+',tkt_number1,flags=0).group()
					ticket_numbers.append(tkt_number2)
		except:
			ticket_numbers = None
			
		
		return ticket_numbers
	
	def ticketed_date(self, data):
		""" Retrieve the ticketed date"""

		try:
			root = jxmlease.parse(data)
			creat_date = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('CreateDateTime')	
			creat_date = creat_date.replace('T',' ')
		except:
			creat_date = None
		return creat_date

	def ticketing_pcc(self, data):
		ticket_pcc_list = []
		tkt_pcc_list = []
		try:
		
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				ticket_pcc1 = node.get_xml_attr('eTicketNumber',"")
				ticket_pcc_list.append(str(ticket_pcc1))
			if ticket_pcc_list == ['']:
				return None
			for i in ticket_pcc_list:
				if i=='':
					pass
				else:
					tkt_pcc = re.search(r"[(/)][A-Z][ ][A-Z0-9_]{4}",i,flags=0).group(0)
					tkt = re.search(r'[ ][A-Z0-9]+',tkt_pcc,flags=0).group()
					return tkt
		except:
			return None

	def ticketing_agent(self, data):
		ticket_agent_list = []
		tkt_agent_list = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				tkt_agent_list1 = node.get_xml_attr('eTicketNumber',"")
				tkt_agent_list.append(str(tkt_agent_list1))
			if tkt_agent_list == ['']:
				return None
			for i in tkt_agent_list:
				if i=='':
					pass
				else:
					try:
						tkt_agent = re.search(r"(/)[A-Z][ ][A-Z0-9_]+[*][A-Z0-9_]+",i,flags=0).group(0)
					except:
						tkt_agent = re.search(r"(/)[A-Z][ ][A-Z0-9_]+",i,flags=0).group(0)
					t_agent = tkt_agent[len(tkt_agent)-3:len(tkt_agent)]
					return t_agent
		except:
			return None
				
	def issue_date(self, data):
		 
		date_list = []
		date_time = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				date_list1 = node.get_xml_attr('eTicketNumber',"")
				date_list.append(str(date_list1))
			for i in date_list:
				if i=='' or 'TV' in i or 'TK' in i :
					pass
				else:
					value =  i.split('/')
					heure = value[-2].split(' ')
					time = value[-1]+' '+heure[-1][0:2]+'H'+heure[-1][2:4]
					date_time.append(time)
		except:
			date_time = None
				
		return date_time
	
	def is_refund(self):

		return

	def is_mco(self):

		return
	

################################### Accounting class ################################################

class Accounting():

	def foi(self):

		foi_list = []
		try:
			print(1)
		except:
			foi_list = ['N/A']
		return foi_list

	def total_amount_list(self, data):
		""" Retrieve a list which total amount """
		
		totalamounts = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				 totalamount1 = node['tir38:TotalFare'].get_xml_attr('Amount')
				 totalamounts.append(str(totalamount1))
		except:
			totalamounts = None
		return 
		
	
	def taxValue(self, data):
		
		tax_value = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare/tir38:Taxes"):
				 tax_value1 = node['tir38:Tax'].get_xml_attr('Amount')
				 tax_value.append(str(tax_value1))
		except:
			tax_value = None
		return tax_value
	
	def taxCode(self, data):
    		
		tax_code = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare/tir38:Taxes"):
				 tax_code1 = node['tir38:Tax'].get_xml_attr('TaxCode')
				 tax_code.append(str(tax_code1))
		except:
			tax_code = None
		return tax_code

	
	
	def commission_list(self, data):
		""" Retrieve a list which contains commission """

		commissions = []
		try:
			for path, _, node in jxmlease.parsedata(data, generator="tir38:AccountingInfo/tir38:PaymentInfo"):
				commission1 = node['tir38:Commission'].get_xml_attr('Amount','')
				commissions.append(str(commission1))
			commissions.remove('')

		except:
			commissions = None
		return commissions



