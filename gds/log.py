# -*- coding: utf-8 -*-

import os
import time
import sqlite3
from os import getcwd,chdir,mkdir


######################## LogXML class ####################
class LogXml():
    
    def __init__(self,pnr,q):
		#Instantiate what we need at the creation of the class
        self.pnr = pnr
        self.q = q

		#Declare a variable for the exact time
        self.times = time.strftime('%HH%M',time.localtime())
		
        #Declare a varaiable for today's date
        self.days = time.strftime('%Y%m%d',time.localtime())
		
    
    def log_xml_Q68(self,data):

        """ The method creates a folder in the current directory if it does not exist, 
            creates an xml file to write what has passed in parameters
        """
        try:
            chdir('V:\\folder_xml')
            
            if os.path.exists(self.days):
                pass
            else:
                folder_name = os.mkdir(self.days)
            chdir(self.days)
            file_name = open(self.pnr+'_'+self.times+'_Q'+str(self.q)+'.xml','w')
            file_name.write(str(data))
            file_name.close()
        except OSError as e:
            print(os.strerror(e.errno))

    
    def log_xml_Q70(self,data):

        """ The method creates a folder in the current directory if it does not exist, 
            creates an xml file to write what has passed in parameters
        """
        try:
            chdir(settings.folder_name_Q70)
            
            if os.path.exists(self.days):
                pass
            else:
                folder_name = os.mkdir(self.days)
            chdir(self.days)
            file_name = open(self.pnr+'_'+self.times+'_Q'+str(self.q)+'.xml','w')
            date_time  = self.days+'/'+self.pnr+'_'+self.times+'_Q'+str(self.q)
            file_name.write(data)
            file_name.close()
        except OSError as e:
            print(os.strerror(e.errno))
        return date_time
 
    

	