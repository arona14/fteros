from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
import pandas as pd
import psycopg2 as pg
from datetime import date
import requests

con = pg.connect("host=ec2-35-171-66-64.compute-1.amazonaws.com dbname=dcrr3f58noacr2 user=u9d5na024rb5gk password=p6c7efd1c875b51bad733a9ee730243755fa16d8763f937ef5a9249a61051b8c7")
con.set_client_encoding('UTF8')

class Command(BaseCommand):
    help = 'synchronize crm data base to trams data base'

    def handle(self, *args, **options):
        to_date = str(date.today())
        rep = requests.post('http://0a5b086f.ngrok.io/api/syntrams/', data = {'to_date': to_date})
        print(rep.content)

