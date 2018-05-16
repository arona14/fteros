# -*- coding: utf-8 -*-

import requests
import jxmlease
from . import myXML
import re

def get_token():
    """ to get sabre token """

    url = "https://webservices3.sabre.com"
    headers = {'content-type': 'text/xml'}

    body = myXML.tokenXML


    response = requests.post(url, data=body, headers=headers)
    r = jxmlease.parse(response.content)
    token = r[u'soap-env:Envelope'][u'soap-env:Header'][u'wsse:Security'][u'wsse:BinarySecurityToken']

    return token

token = get_token()
#token ='Shared/IDL:IceSess\/SessMgr:1\.0.IDL/Common/!ICESMS\/RESC!ICESMSLB\/RES.LB!-3212749367979084401!1793194!0'

class Pnr(object):

    
    def display_pnr(self, pnr):
        """ display the pnr to get xml file """ 

        url = "https://webservices3.sabre.com"
        headers = {'content-type': 'text/xml; charset=utf-8'}
        body = myXML.readItin % (token, pnr)
        response = requests.post(url, data=body, headers=headers)
        ressource = response.content
        return ressource
    
    def send_sabre_entry(self, token, command):
        """ to send sabre command """
        
        url = "https://webservices3.sabre.com"
        headers = {'content-type': 'text/xml'}
        body = myXML.sabreCommand % (token, command)
        body = body.encode('utf-8')
        response = requests.post(url, data=body, headers=headers)
        r = jxmlease.parse(response.content)

        sabreResponse = r[u'soap-env:Envelope'][u'soap-env:Body'][u'SabreCommandLLSRS'][u'Response']

        return sabreResponse.encode('utf-8')

    def list_of_pnr_in_q(self,q):
        """ return list of pnr in the Q """
    
        entry = 'Q/' + str(q) + '/L'
        resp = str(Pnr().send_sabre_entry(token, entry))
        line = resp.split('\n')
        x = []
        for i in range(len(line)):
            try:
                pnr = re.search(r'  [A-Z]{6}  ', line[i], flags=0).group()
            except:
                pnr = ""
            if len(pnr) > 1:
                y = re.search(r'[A-Z]{6}', pnr, flags=0).group()
                x.append(y)
        #print(x)
        return x



