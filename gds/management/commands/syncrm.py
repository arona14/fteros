from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
import pandas as pd
import psycopg2 as pg
from datetime import datetime,date
import requests

con = pg.connect("host=ec2-35-171-66-64.compute-1.amazonaws.com dbname=dcrr3f58noacr2 user=u9d5na024rb5gk password=p6c7efd1c875b51bad733a9ee730243755fa16d8763f937ef5a9249a61051b8c7")
con.set_client_encoding('UTF8')

def get_max_date():
    #try:
    sqls = "SELECT Max(updated) FROM crm_customer "
    df = pd.read_sql(sql=sqls, con=con)
    md = df['max'][0]
    md = str(md).split(' ')
    return md[0]
    #except:
    #    return None
class Command(BaseCommand):
    help = 'synchronize crm data base to trams data base'

    def handle(self, *args, **options):
        from_date = get_max_date()
        to_date = str(date.today())
        print(from_date, to_date)
        #last_update = datetime.strptime(last_update,"%Y-%m-%d")
        
        rep = requests.post('http://cosmo.com.ngrok.io/api/syncrm/', data = {'from_date': '2018-03-15', 'to_date': to_date})
        print(rep.content)

