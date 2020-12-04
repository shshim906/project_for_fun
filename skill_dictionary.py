# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:55:55 2020

@author: shshi

This script is used to obtain ffxiv skills
"""
# --- import ---

import pandas as pd
import os
import re
import tkinter as tk

# --- functions ---
def split_filename(filename):
    return re.split('[\\\. ]',filename)

path='E:\\ffxiv_dps_rotation_simul\\skill_icons'
files = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith(('.png','jpeg'))]

skillnames=[]
for file in files:
    skillnames.append([split_filename(file)[-4],
                       split_filename(file)[-3],
                       split_filename(file)[-2],
                       file])
    
job_skills = pd.DataFrame(skillnames,columns=['job','lv','skills','name'])

job_function=list()

for job in job_skills['job']:
    if job in ['ast','whm','sch']:
        job_function.append('heal')
    elif job in ['pld','war','drk','gnb']:
        job_function.append('tank')
    elif job in ['brd','mch','dnc']:
        job_function.append('ranged')
    elif job in ['blm','smn','rdm']:
        job_function.append('magic')
    elif job in ['mnk','drg','nin','sam']:
        job_function.append('melee')
    else:
        job_function.append(job)

job_skills['job_function']=job_function


job_skills.to_excel('ffxivjob.xlsx',index=False)

