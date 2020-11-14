# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:52:13 2020

@author: YVAN-FRANCO
"""

import pandas as pd
import numpy as np


data = pd.read_json('communes.json')
data = data.to_dict('records')
"""for commune in data:
    nameCom = commune["name"]
    fkt = commune["fokontany"]
    for fkts in fkt:
        print(fkts["name"])"""
for fokontany in data:
    fktn = fokontany["fokontany"]
    print(fktn)
    


    

