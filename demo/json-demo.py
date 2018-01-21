# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:02:58 2018

@author: Administrator
"""

import json

data =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } 

jsondata = json.dumps(data)
print(type(jsondata))
print (jsondata)

originaldata = json.loads(jsondata)
print(type(originaldata))
print (originaldata)
