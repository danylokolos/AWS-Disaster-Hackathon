# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:55:37 2022

@author: Danylo
"""

#%% Code to read JSON file

import os
import json
import pandas as pd  

FilePath = 'C:/Users/Danylo/Documents/Projects/2021-12-AWSDisasterHackathon/Tweets/'
files = os.listdir(FilePath)

small_dfs = []
for ii in files:
    FileToOpen = FilePath + ii
    f = open(FileToOpen,encoding='utf-8')
    data = json.load(f)
    small_dfs.append(pd.json_normalize(data['data']))
    f.close()
df = pd.concat(small_dfs, ignore_index=True)
    





#FileToOpen = 'C:/Users/Danylo/Documents/Projects/2021-12-AWSDisasterHackathon/Tweets/100-1Tweets - earthquake - Jan 11 2022 -'
#f = open(FileToOpen,encoding='utf-8')
#data = json.load(f)
#df = pd.json_normalize(data['data'])
#f.close()