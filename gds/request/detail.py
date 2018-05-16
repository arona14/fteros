#coding: utf-8
import pandas as pd
import smtplib
from gds.models import SegmentSched,SchedChange
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def getListDepartureArrival(list_data):
    new_list = []
    for i in list_data:
        new_list.append(datetime.strptime(i[0:16], '%Y-%m-%d %H:%M').strftime('%d%b %H:%M'))
    return new_list

    
class Mail(object):
    def sendMail(self,toaddr,pnr_value):
        new_departure = []
        new_arrival = []
        fromaddr = "virginielamesse@gmail.com"
        list_detail = SegmentSched.objects.filter(pnr=pnr_value)   
        list_sched_change =  SchedChange.objects.filter(pnr=pnr_value)
        airline = []
        departure =[]
        arrival = []
        fligthno = []
        status =[]
        pax_name =[]
        origin = []
        destination = []
        for i in list_detail:
            airline.append(i.airline)
            origin.append(i.origin)
            destination.append(i.destination)
            departure.append(i.departure_date)
            arrival.append(i.arrival_date)
            status.append(i.status)
            fligthno.append(i.fligthno)
        for d in departure:
            new_departure.append(str(d))
        for a in arrival:
            new_arrival.append(str(a))
            
        departure = getListDepartureArrival(new_departure)
        arrival = getListDepartureArrival(new_arrival)

        df = pd.DataFrame({'Airline':airline,'Fligthno':fligthno,'Origin':origin,
        'Departure':departure,'Dest':destination,'Arrival':arrival,'Status':status},columns=['Airline','Fligthno','Origin','Departure','Dest','Arrival','Status'])
        df2=df.to_html(bold_rows=True, index=False,border='0px',justify='center')
    
        b = list_sched_change[0].pax_names
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
            </html>""".format(pnr_value,b,df2)
        message = MIMEMultipart("alternative", None,  [MIMEText(html,'html')])
        message['Subject'] = "Schedule Change"
        message['From'] = fromaddr
        message['To'] = toaddr
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("virginielamesse@gmail.com", "tidianesy")
        server.sendmail(fromaddr, toaddr, message.as_string())
        server.quit()
