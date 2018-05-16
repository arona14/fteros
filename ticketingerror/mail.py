# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pandas as pd
import psycopg2 as pg
import pandas as pd
import sys 
import smtplib

from datetime import date, timedelta, datetime,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

connexion = pg.connect("host=ec2-35-171-66-64.compute-1.amazonaws.com dbname=dcrr3f58noacr2 user=u9d5na024rb5gk password=p6c7efd1c875b51bad733a9ee730243755fa16d8763f937ef5a9249a61051b8c7")
cur = connexion.cursor()


def userEmail(sign):
    try:

        user_value = []
        df1 = """SELECT email FROM crm_user u INNER JOIN crm_sign s ON u.id=s.user_id WHERE s.value = '{}' """.format(sign)
        df2 = pd.read_sql(sql=df1, con=connexion)
        for index, row in df2.iterrows():
            user_value.append({'id':str(row[0])})
        for value in user_value[0].values():
            return value
    except:
        return None


def customerEmail(dk):
    try:
        email_value = []

        df1 = """SELECT email FROM crm_customer WHERE interface_id = '{}' """.format(dk)
        df2 = pd.read_sql(sql=df1, con=connexion)
        for index, row in df2.iterrows():
            email_value.append({'id':str(row[0])})
        for value in email_value[0].values():
            return value
    except:
        return None


def fullNameUser(sign):
    user_value = []
    df1 = """SELECT first_name,last_name FROM crm_user u INNER JOIN crm_sign s ON u.id=s.user_id WHERE s.value = '{}' """.format(sign)
    df2 = pd.read_sql(sql=df1, con=connexion)
    for index, row in df2.iterrows():
        user_value.append(str(row[0]))
        user_value.append(str(row[1]))
    return '  '.join(user_value)
class Mail(object):
    def sendMailUser(self,sign,pnr_value,remark):
        fromaddr = "cosmo@ctsfares.com"
        to = userEmail(sign)
        cc = ["portal@ctsfares.com"]
        remark = '<br/>'.join(list(remark))
    
        html = """
            <html>
                <body>
                    <p>DO NOT REPLY TO THIS EMAIL</p>
                    <p></p>
                    <p>Hello {},</p>
                    <p></p>
                    <p>There was an error issuing your PNR {} due below reason(s):</p>
                    <p></p>
                    <p>{}</p>
                    <p></p>
                    <p>Thank you</p>
                    <p>Cosmo</p>
                </body>
            </html>""".format(fullNameUser(sign),pnr_value,remark)
        message = MIMEMultipart("alternative", None,  [MIMEText(html,'html')])
        message['Subject'] = "Autoticketing error for {} ".format(pnr_value)
        message['From'] = fromaddr
        message['To'] = to
        toaddr = [to] + cc
        server = smtplib.SMTP('smtp.office365.com',587)
        server.starttls()
        server.login(fromaddr, 'Ctsf@res2018')
        server.sendmail(fromaddr,toaddr, message.as_string())
        server.quit()

    def sendMailCustomer(self,dk,pnr_value,remark):
        fromaddr = "cosmo@ctsfares.com"
        to = customerEmail(dk)
        cc = ["portal@ctsfares.com"]
        remark = '<br/>'.join(list(remark))
    
        html = """
            <html>
                <body>
                    <p>DO NOT REPLY TO THIS EMAIL</p>
                    <p></p>
                    <p>Hello,</p>
                    <p></p>
                    <p>There was an error issuing your PNR {} due below reason(s):</p>
                    <p></p>
                    <p>{}</p>
                    <p></p>
                    <p>Thank you</p>
                    <p>Cosmo</p>
                </body>
            </html>""".format(pnr_value,remark)
        message = MIMEMultipart("alternative", None,  [MIMEText(html,'html')])
        message['Subject'] = "Autoticketing error for {} ".format(pnr_value)
        message['From'] = fromaddr
        message['To'] = to
        toaddr = [to] + cc
        server = smtplib.SMTP('smtp.office365.com',587)
        server.starttls()
        server.login(fromaddr, 'Ctsf@res2018')
        server.sendmail(fromaddr,toaddr, message.as_string())
        server.quit()
    
    def sendMailAdmin(self,pnr_value,remark):
        fromaddr = "cosmo@ctsfares.com"
        to = "malick@ctsfares.com"
        cc = ["portal@ctsfares.com"]
        remark = '<br/>'.join(list(remark))
    
        html = """
            <html>
                <body>
                    <p>DO NOT REPLY TO THIS EMAIL</p>
                    <p></p>
                    <p>Hello,</p>
                    <p></p>
                    <p>There was an error issuing your PNR {} due below reason(s):</p>
                    <p></p>
                    <p>{}</p>
                    <p></p>
                    <p>Thank you</p>
                    <p>Cosmo</p>
                </body>
            </html>""".format(pnr_value,remark)
        message = MIMEMultipart("alternative", None,  [MIMEText(html,'html')])
        message['Subject'] = "Autoticketing error for {} ".format(pnr_value)
        message['From'] = fromaddr
        message['To'] = to
        toaddr = [to] + cc
        server = smtplib.SMTP('smtp.office365.com',587)
        server.starttls()
        server.login(fromaddr, 'Ctsf@res2018')
        server.sendmail(fromaddr,toaddr, message.as_string())
        server.quit()

