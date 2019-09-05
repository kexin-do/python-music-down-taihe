# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:43:46 2018

@author: root
"""
count = 0;
class musicDownObject:
    
    def __init__(self,json_object,index):
        self.sname = json_object['sname'].replace('&lt;em&gt;','').replace('&lt;/em&gt;','')
        self.sid = str(json_object['sid'])
        self.author = json_object['author'].replace('&lt;em&gt;','').replace('&lt;/em&gt;','')
        self.oid = str(json_object['oid'])
        self.pay_type = json_object['pay_type']
        self.isJump = json_object['isJump']
        self.is_down = 0
        self.index = index;