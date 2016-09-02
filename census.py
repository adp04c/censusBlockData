# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:11:36 2016

@author: AustinPeel
"""
import requests 
import json

class censusData:
    
    def __init__(self,lat,lon,showall=True):
        url = 'http://data.fcc.gov/api/block/find?format=json' 
        payload = {'latitude': lat,'longitude': lon,'showall': showall}       
        self.r  = requests.get(url, params=payload)
        self.y = self.r.json()
    
    def block(self):
        return str(self.y['Block']['FIPS'])
    
    def county(self):
        return str(self.y['County']['name'])
    
    def state(self):
        return str(self.y['State']['name'])
    
    def intersection(self):
        records = []        
        for  b in self.y['Block']['intersection']:       
            record = filter(lambda x: x.isdigit(), str(b))
            records.append(record)
        return records   
    def data(self):
        return json.dumps(self.y)      
        




