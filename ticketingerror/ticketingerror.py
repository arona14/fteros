# -*- coding: utf-8 -*-

import os
import re
import requests
import numpy as np
from pnr import Pnr, token

class TicketingError(object):

    def get_agent(self, resp):
        s = 'ON  WR17 0123/000'
        agent = {}
        line = resp.split('\n')
        for i in range(len(line)):
            try:
                p = re.search(s,line[i], flags=0).group()
            except:
                p = ""
            if len(p) > 1:
                s = line[i]
                break
        try:
            pcc = re.search(r"BY [A-Z0-9]{4}",s, flags=0).group()
        except:
            pcc = ""
        if len(pcc)>1:
            pcc1 =  re.search(r"[A-Z0-9]{4}",s, flags=0).group()
            agent['pcc'] = pcc1
        s = str(s)
        try:
            sign = re.search(r"  [A-Z]{3}",s, flags=0).group()
        except:
            sign = ""
        if len(sign)>1:
            agent['sign'] = re.search(r"[A-Z]{3}",sign, flags=0).group()
            return agent

    def get_remarks(self, resp):
        t = 'PRTL'
        remarks = []
        line = resp.split('\n')
        for i in range(len(line)):
            try:
                r = re.search(t,line[i], flags=0).group()
            except:
                r = ""
            if len(r) > 1:
                index = line[i].find (t)
                index = index + len(t)
                s = line[i][index:len(line[i])]
                remarks.append(s)
        return remarks

    def get_dk(self, resp):
        t = 'CUSTOMER NUMBER'
        line = resp.split('\n')
        try:
            for i in range(len(line)):
                try:
                    r = re.search(t,line[i], flags=0).group()
                except:
                    r = ""
                if len(r) > 1:
                    s = line[i]
            dk =  re.search(r"[A-Z0-9]{10}",s, flags=0).group()
            return dk
        except:
            return None