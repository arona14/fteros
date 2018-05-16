from django.core.management.base import BaseCommand, CommandError
from gds.models import SchedChange, SegmentSched
from gds.pnr import Pnr, token
from gds.reservation import *
from datetime import datetime
import psycopg2 as pg
from gds.log import LogXml

connexion = pg.connect("host=ec2-35-171-66-64.compute-1.amazonaws.com dbname=dcrr3f58noacr2 user=u9d5na024rb5gk password=p6c7efd1c875b51bad733a9ee730243755fa16d8763f937ef5a9249a61051b8c7")
cur = connexion.cursor()

def listPnrSchedchange():
    list_pnr = []
    query = """ SELECT pnr FROM gds_schedchange"""
    df1 = pd.read_sql(sql=query, con= connexion)
    for index, row in df1.iterrows():
        list_pnr.append(str(row[0]))
    return list_pnr


def deleteSchedchange(pnr):
    	
	cur.execute("DELETE FROM gds_schedchange WHERE pnr=%s",(pnr,))
	connexion.commit()

def deleteSegmentched(pnr):
	cur.execute("DELETE FROM gds_segmentsched WHERE pnr_id=%s",(pnr,))
	connexion.commit()

class Command(BaseCommand):
    help = 'Fetch the schedule changes in Q70 - Custom commannd'

    def handle(self, *args, **options):
       
        list_pnr = listPnrSchedchange()

        for i in list_pnr:
            obj_xml = Pnr().display_pnr(i)
            status_list = Itinerary().segment_status_list(obj_xml)

            if status_list != [] and status_list != ['N/A'] :
                print(i)
            else:    
                l = LogXml(i,'70')
                l.log_xml_Q68(obj_xml)
                deleteSegmentched(i)
                deleteSchedchange(i)

                    