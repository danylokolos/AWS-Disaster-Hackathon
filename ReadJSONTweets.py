# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:55:37 2022

@author: Danylo
"""

#%% Code to read JSON tweet file

import os
import json
import pandas as pd  

# folder with all tweet files
FilePath = 'C:/Users/Danylo/Documents/Projects/2021-12-AWSDisasterHackathon/Codes/Tweets/'


files = os.listdir(FilePath)

# loop over all files
small_dfs = []
for ifile in files:
    FileToOpen = FilePath + ifile
    f = open(FileToOpen,encoding='utf-8')
    data = json.load(f)
    small_dfs.append(pd.json_normalize(data['data']))
    f.close()

# combine into one dataframe
df = pd.concat(small_dfs, ignore_index=True)
    
