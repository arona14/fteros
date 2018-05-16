#coding: utf-8
from .reservation import Itinerary,Passenger
from .pnr import Pnr,token

import pandas as pd
import sys 
import jxmlease
import smtplib
import tabulate
import os
from os import chdir
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from astropy.table import Table, Column
import numpy as np

p = Pnr()
q = 70
list_pnr = p.list_of_pnr_in_q(q)

class Mail(object):
    def __init__(self,pnr):
        self.pnr = pnr
    def sendMail(self,toaddr):
        fromaddr = "virginie@ctsfares.com"
        data = Pnr().display_pnr(self.pnr)
        pnr = self.pnr
        if pnr in list_pnr:
                
            status = Itinerary().segment_status_list(data)
            name = Passenger().full_name_list(data)
            arrival_date = Itinerary().arrival_datetime_list(data)
            departure_date = Itinerary().departure_datetime_list(data)
            origin = Itinerary().origin_city_list(data)
            destination = Itinerary().destination_city_list(data)
            status = Itinerary().segment_status_list(data)
            flightno = Itinerary().flight_number_list(data) 
            airline = Itinerary().airline_list(data)
            t=Table([airline, flightno, origin, destination,departure_date,status,arrival_date], names=('Airline','Fligthno','Origin','Dest','Departure', 'Status','Arrival'))
            df = t.to_pandas()
            df2=df.to_html(bold_rows=True, index=False,border='0px')
            
            b = ",".join(name)
            html = """
                <html>
                    <body>
                        <p>Hello,</p>
                        <p>There might be a schedule change affecting your reservation:</p>
                        <p>PNR:{}</p>
                        <p>Passenger:</p>
                        <p>{}</p>
                        <table>{}<!table>
                    </body>
                </html>""".format(pnr,b,df2)
            message = MIMEMultipart("alternative", None,  [MIMEText(html,'html')])
            message['Subject'] = "Schedule Change"
            message['From'] = fromaddr
            message['To'] = toaddr
            
            server = smtplib.SMTP('smtp.office365.com',587)
            server.starttls()
            server.login("virginie@ctsfares.com", "Tidianesy49")
            server.sendmail(fromaddr, toaddr, message.as_string())
            server.quit()



