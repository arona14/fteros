# -*- coding: utf-8 -*-
import pandas as pd
import jxmlease
import datetime
import re



####################################### Itinerary class ##################################
class Itinerary(object):

	
	def segment_status_list(self, data):
		""" Retrive a list wich contains all status codes
			for each segment """

		status_code = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				s = node.get_xml_attr('Status')
				status_code.append(str(s))
		except:
			status_code = ['N/A']
	
		return status_code
	

	def airline_list(self, data):
		""" Retrieve a list which contains all airlines for each segment"""
		
		airline = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				a1 = node['tir38:MarketingAirline'].get_xml_attr('Code')
				airline.append(str(a1))	
		except:
			airline = ['N/A']
	
		return 
		
	def carrier_list(self, data):
		""" Retrieve a list which contains all airlines for each segment"""
		
		carrier = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				c1 = node['tir38:OperatingAirline'].get_xml_attr('Code')
				carrier.append(str(c1))
		except:
			carrier = ['N/A']
	
		return carrier


	def origin_city_list(self, data):
		""" Retrieve a list which contains origines
			city list for each segment """

		
		origin_location = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				origin_location1 = node['tir38:OriginLocation'].get_xml_attr('LocationCode')
				origin_location.append(str(origin_location1))
		except:
			origin_location = ["N/A"]

		return origin_location 


	def destination_city_list(self, data) :
		""" Retrieve a list which contains destination city
			for each segment """ 

		destination_location = []
		try:

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				destination_location1 = node['tir38:DestinationLocation'].get_xml_attr('LocationCode')
				destination_location.append(str(destination_location1))
	
		except:
			destination_location = ["N/A"]
		
		return destination_location 


	def flight_number_list(self, data):
		""" This methode retrieve a list wich combers 
		of flight for each segment """

		flight_number = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				f = node['tir38:OperatingAirline'].get_xml_attr('FlightNumber')
				flight_number.append(str(f))
		except:
			flight_number = ['N/A'] 
			
		return flight_number

	def class_of_service_list(self, data):
		""" This methode retrieve a list wich combers 
		of flight for each segment """

		class_of_service = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				class_of_service1 = node.get_xml_attr('ResBookDesigCode')
				class_of_service.append(str(class_of_service1))
		except:
			class_of_service = ['N/A'] 
			
		return class_of_service


	def flight_duration_list(self, data):
		""" This method retrieve a list which contains flight duration """

		time = []
		try:
			
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				time1 = node.get_xml_attr('ElapsedTime')
				time.append(str(time1))
		except:
			time = ['N/A'] 
		return time

	def departure_datetime_list(self, data):
		""" Return list wich contains departure datetime """

		departure_datetime = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				departure_datetime1 = node.get_xml_attr('DepartureDateTime')
				departure_datetime.append(str(departure_datetime1))
		except:
			departure_datetime = ['N/A']
		return departure_datetime


	def arrival_datetime_list(self, data):
		""" Retrieve list wich contains arrival datetimes """

		datetime = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				datetime1 = node.get_xml_attr('ArrivalDateTime')
				datetime.append(str(datetime1))
		except:
			datetime = ['N/A']
		return datetime
	

	def updated_depature_datetime(self, data):
		""" Retrieve list wich contains updated depature datetimes """

		update_datetime = []

		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ReservationItems/tir38:Item/tir38:FlightSegment"):
				datetime1 = node['tir38:UpdatedDepartureTime']
				update_datetime.append(str(datetime1))
		except:
			update_datetime = ['N/A']
		return update_datetime

	def get_pnr(self, data):
		""" get the agency's dk """

		try:
			root = jxmlease.parse(data)
			pnr = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef'].get_xml_attr('ID')
		except:
			pnr = ['N/A']
		return pnr
	

	def miscsegment_list(self, data):
		""" Retrieve list which contains all messages text
			from  MiscSegment """ 

		msg_list = []

		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ReservationItems/tir38:Item/tir38:MiscSegment/tir38:Text"):
				t = node
				msg_list.append(str(t))
			
		except:
			msg_list = ['N/A']
		return msg_list
		
	def miscsegment_status(self, data):
		""" Retrieve list which contains all status
			from  MiscSegment """ 

		msg_status = []

		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ReservationItems/tir38:Item/tir38:MiscSegment"):
				t = node.get_xml_attr('Status')
				msg_status.append(str(t))
		except:
			msg_list = []
		return msg_status

	def validating_carrier(self, data):
		"""Return the validating carrier for this reservation"""

		validatingcarrier = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:PriceQuote/tir38:PricedItinerary"):
				validatingcarrier1 = node.get_xml_attr('ValidatingCarrier')
				validatingcarrier.append(str(validatingcarrier1))
		except:
			validatingcarrier = ['N/A']
		return validatingcarrier

	def return_date(self, data):
		"""Return the validating carrier for this reservation"""
		validatingcarrier = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:PriceQuote/tir38:PricedItinerary"):
				validatingcarrier1 = node.get_xml_attr('ValidatingCarrier')
				validatingcarrier.append(str(validatingcarrier1))
		except:
			validatingcarrier = ['N/A']

		#print validatingcarrier
		return validatingcarrier[0]

	def frequent_flyer(self, data):
		""" get the return fidelity """

		try:
			root = jxmlease.parse(data)
			frequent = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:CustomerInfo']['tir38:CustLoyalty'].get_xml_attr('MembershipID')
		except:
			frequent = ['N/A']
		return frequent
	
################################### Passenger class ####################################

class Passenger(object):

	def first_name_list(self, data):
		""" Retrieve a list which contains all passengers firstname 
			for each segment """

		first_name= []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				
				first_name1 = node['tir38:GivenName']
				first_name.append(str(first_name1))
		except:
			first_name = ['N/A']
		return first_name
		

	def surname_list(self, data):
		""" Retrieve a list which contains all passengers surname 
			for each segment """

		surname= []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				
				surname1 = node['tir38:Surname']
				surname.append(str(surname1))
		except:
			surname = ['N/A']
		return surname	

	def full_name_list(self,data):
		""" Retrieve a list which contains all passengers fullname 
			for each segment """

		full_name = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				
				full_name1=node['tir38:GivenName']+ ' '+node['tir38:Surname']
				full_name.append(str(full_name1))
		except:
			full_name = ['N/A']
		return full_name
	
	def passenger_type_list(self, data):
		""" this method contains list of all passenger type"""

		pass_type = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:PersonName"):
				pass_type1 = node.get_xml_attr('PassengerType')
				pass_type.append(str(pass_type1))
		except:
			pass_type = ['N/A']
		return pass_type

	def date_of_birth_list(self, data):
		""" this method retrieve the list of passengers's date of birth """

		birth_day = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				if node.get_xml_attr('SSR_Type') == "DOCS":
					bd = str(node['tir38:Text'])
					#string = bd.split('/')
					#dob_list.append(string[5])
					birth = re.search(r"[0-9]{2}[A-Z]{3}[0-9]{4}",bd,flags=0).group()
					birth_day.append(birth)
				
		except:
			birth_day = ['N/A']

		return birth_day

	def email_list(self, data):
		""" this method retrieve the list of passengers's date of birth """
		try:
			mail = []

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				if node.get_xml_attr('SSR_Type') == "CTCE":
					bd = str(node['tir38:Text'])
					string = re.search(r'[\w\.-]+//[\w\.-]+',bd).group(0)
					email = string.replace('//','@')
					mail.append(email)
		except:
			mail = ['N/A']
				
		return mail

	def phone_list(self, data):
		""" this method retrieve the list of passengers's date of birth """
		try:
			phone = []

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				if node.get_xml_attr('SSR_Type') == "CTCM":
					bd = str(node['tir38:Text'])
					phone1 = re.search(r'[0-9]{5,}',bd).group(0)
					phone.append(phone1)
		except:
			phone = ['N/A']
				
		return phone

	def gender_list(self, data):
		""" this method allows to know the list of passenger's gender """

		g_list = []

		try:

			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:SpecialServiceInfo/tir38:Service"):
				if node.get_xml_attr('SSR_Type') == "DOCS":
					bd = str(node['tir38:Text'])
					string = bd.split('/')
					for i in string:
						if i=="F" or i=="M":
							gender=i
					
		except:
			string = ['N/A']
		return gender

	
###################################### Agency class ######################################

class Agency(object):


	def agency_dk(self, data):
		""" get the agency's dk """

		try:
			root = jxmlease.parse(data)
			dk = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef'].get_xml_attr('CustomerIdentifier')
		except:
			dk = ['N/A']
		return dk


	def agency_phone_list(self, data):
		""" retrieve the phone list of agency"""

		phone = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:CustomerInfo/tir38:ContactNumbers/tir38:ContactNumber"):
				phone1 = node.get_xml_attr("Phone")
				phone.append(str(phone1))
		except:
			phone = ['N/A']
		return phone
	
	def agency_address(self, data):
		""" this method retrieve a list which contains agency addresses """

		addressline = []
		try:
			for path, _, node in jxmlease.parse(data,generator="tir38:CustomerInfo/tir38:ContactNumbers/tir38:ContactNumber"):
				addressline1 = node.get_xml_attr('LocationCode')
				addressline.append(str(addressline1))
		except:
			addressline = ['N/A']
		return addressline

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
		""" get the agency's dk """

		try:
			root = jxmlease.parse(data)
			pcc = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('AAA_PseudoCityCode')
		except:
			pcc = ['N/A']
		return pcc

	def agency_create(self, data):
		""" get the agency's dk """

		try:
			root = jxmlease.parse(data)
			agent = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('CreationAgent')
		except:
			agent = ['N/A']
		return agent

########################################### Pricing class #####################################

class Pricing(object):
	
	def  base_fare_list(self, data):
		"""This methed return the base fare list for this reservation"""

		basefare = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				basefare1 = node['tir38:BaseFare'].get_xml_attr('Amount')
				basefare.append(str(basefare1))
		except:
			basefare = ['N/A']
		return basefare

	def total_fare_list(self, data):
		""" this method retrieve a list which contains totals fares for this reservation  """

		totalfare = []
		try:
			 for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				 totalfare1 = node['tir38:TotalFare'].get_xml_attr('Amount')
				 totalfare.append(str(totalfare1))

		except:
			totalfare = ['N/A']
		return totalfare
	
	
	def tax_detail(self):

		taxdetail = []
		try:
			print(1)
		except:
			taxdetail = ['N/A']
		return taxdetail
	
	def total_tax(self, data):
		""" Retrieve a list which contains total tax for this reservation """

		totaltax = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				totaltax1 = node['tir38:Totals']['tir38:Taxes']['tir38:Tax'].get_xml_attr('Amount')
				totaltax.append(totaltax1)
			
		except:
			totaltax = ['N/A']
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
			payement = ['N/A']
		return payement

############################################ Rules class #################################################

class Rules():


	def baggage_allowance(self, data):
		""" Retrieve a list which contains baggage allowance """

		baggage = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:ItineraryPricing/tir38:PriceQuote/tir38:PricedItinerary/tir38:AirItineraryPricingInfo/tir38:PTC_FareBreakdown/tir38:FlightSegment"):
				baggage1 = node['tir38:BaggageAllowance'].get_xml_attr("Number","")
				baggage.append(str(baggage1))
			baggage.remove('')
		except:
			pass 	
		return baggage

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
				#print ticket_number_list
			for i in ticket_number_list:
				#print i
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
			exchange_list = ['N/A']
		return exchange_list
	
	def ticketed_number_list(self, data):
		""" Retrieve a list which contains ticket number """

		ticket_number_list = []
		tkt_number_list = []
		try:
		
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				ticket_number = node.get_xml_attr('eTicketNumber',"")
				ticket_number_list.append(str(ticket_number))
			for i in ticket_number_list:
				if i=='':
					pass
				else:

					tkt_numbers = re.search(r"(TE)[ ][0-9]+",i,flags=0).group(0)

					tkt_number = re.search(r'[0-9]+',tkt_numbers,flags=0).group()
					tkt_number_list.append(tkt_number)
		except:
			tkt_number_list = ['N/A']
			
		
		return tkt_number_list
	
	def ticketed_date(self, data):
		""" Retrieve the ticketed date"""

		try:
			root = jxmlease.parse(data)
			creat_date = root['soap-env:Envelope']['soap-env:Body']['tir38:TravelItineraryReadRS']['tir38:TravelItinerary']['tir38:ItineraryRef']['tir38:Source'].get_xml_attr('CreateDateTime')	
		except:
			creat_date = 'NA'
		return creat_date

	def ticketing_pcc(self, data):
		ticket_pcc_list = []
		tkt_pcc_list = []
		try:
		
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				ticket_pcc1 = node.get_xml_attr('eTicketNumber',"")
				ticket_pcc_list.append(str(ticket_pcc1))
			for i in ticket_pcc_list:
				if i=='':
					pass
				else:
					tkt_pcc = re.search(r"[(/)][A-Z][ ][A-Z0-9_]{4}",i,flags=0).group(0)
					tkt = re.search(r'[ ][A-Z0-9]+',tkt_pcc,flags=0).group()
					return tkt
		except:
			return 'None'

	def ticketing_agent(self, data):
		ticket_agent_list = []
		tkt_agent_list = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
				tkt_agent_list1 = node.get_xml_attr('eTicketNumber',"")
				tkt_agent_list.append(str(tkt_agent_list1))
			for i in tkt_agent_list:
				if i=='':
					pass
				else:
					tkt_agent = re.search(r"(/)[A-Z][ ][A-Z0-9_]+",i,flags=0).group(0)
					t_agent = tkt_agent[len(tkt_agent)-3:len(tkt_agent)]
					return t_agent
		except:
			return 'None'
				
	def issue_date(self, data):
		ticket_agent_list = []
		tkt_agent_list = []
		for path, _, node in jxmlease.parse(data, generator="tir38:TravelItinerary/tir38:ItineraryInfo/tir38:Ticketing"):
			tkt_agent_list1 = node.get_xml_attr('eTicketNumber',"")
			tkt_agent_list.append(str(tkt_agent_list1))
			print(tkt_agent_list)
		for i in tkt_agent_list:
			if i=='':
				pass
			else:
				tkt_agent = re.search(r"([0-9](/)[A-Z0-9_]+",i,flags=0).group(0)
				print(tkt_agent)
		#return ticket_agent_list
	
		
	
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
		
		totalamount = []
		try:
			for path, _, node in jxmlease.parse(data, generator="tir38:ItinTotalFare"):
				 totalamount1 = node['tir38:TotalFare'].get_xml_attr('Amount')
				 totalamount.append(str(totalamount1))
		except:
			totalamount = ['N/A']
		return totalamount
	
	def commission_list(self, data):
		""" Retrieve a list which contains commission """

		commission_list = []
		try:
			for path, _, node in jxmlease.parsedata(data, generator="tir38:AccountingInfo/tir38:PaymentInfo"):
				commission_list1 = node['tir38:Commission'].get_xml_attr('Amount','')
				commission_list.append(str(commission_list1))
			commission_list.remove('')

		except:
			commission_list = ['N/A']
		return commission_list



