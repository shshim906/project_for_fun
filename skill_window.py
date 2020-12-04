# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:22:41 2020

@author: shshi
"""

# --- import ---

import pandas as pd
import os
import re
import tkinter as tk
import math
from PIL import ImageTk, Image


# --- functions ---
def split_filename(filename):
    return re.split('[\\\. ]',filename)

# Empty a list
def pop_all(l):
    r, l[:] = l[:], []
    return r

path='E:\\ffxiv_dps_rotation_simul\\skill_icons'
files = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith(('.png','jpeg'))]

# skillnames=[]
# for file in files:
#     skillnames.append([split_filename(file)[-4],
#                        split_filename(file)[-3],
#                        split_filename(file)[-2],
#                        file])
    
# job_skills = pd.DataFrame(skillnames,columns=['job','lv','skills','name'])

job_skills=pd.read_excel('output.xlsx')

job_function=list()

for job in job_skills['job']:
    if job in ['ast','whm','sch','HealerRollAction']:
        job_function.append('heal')
    elif job in ['pld','war','drk','gnb','TankRollAction']:
        job_function.append('tank')
    elif job in ['brd','mch','dnc','PhysicalRangedRollAction']:
        job_function.append('ranged')
    elif job in ['blm','smn','rdm','MagicalRangedRollAction']:
        job_function.append('magic')
    elif job in ['mnk','drg','nin','sam','MeleeRollAction']:
        job_function.append('melee')
    else:
        job_function.append(job)

job_skills['job_function']=job_function



root = tk.Tk()
root.title("Let's practice FFXIV dps rotation")

# create frame where buttons can be placed in
root.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1)
root.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], weight=1)

classskill=tk.Label(root,text="Class skills")
classskill.grid(row=1,column=1,sticky='nsew')

# make a grid
#def populate_grid(job):
job='pld'
grid_list=list()
chosen_job=job_skills[job_skills['job']==job]
special_list=chosen_job[~chosen_job['special skill'].isnull()]['skills']
skill_list=chosen_job[chosen_job['special skill'].isnull()]['skills']
    
rows=math.ceil(len(skill_list)/8)
for i in range(rows):
    grid_list.append(skill_list[:8].tolist())
    skill_list=skill_list[8:]

add_grid_list=list()
special_rows=math.ceil(len(special_list)/8)
for i in range(special_rows):
    add_grid_list.append(special_list[:8].tolist())
    special_list=special_list[8:]


rotation_list=list()

# make a button to confirm the rotation
back_button = tk.Button(root, text='back',
                        bg='azure', command=rotation_list.pop)

back_button.grid(row=0, column=2, sticky="nsew")


#make a button to remove the last skill added to the rotation list
back_button = tk.Button(root, text='back',
                        bg='azure', command=rotation_list.pop)

back_button.grid(row=0, column=2, sticky="nsew")

# make a button to clear the rotation made
clear_button = tk.Button(root, text='Clear',
                         bg='yellow', command= lambda l=rotation_list: pop_all(l))

clear_button.grid(row=0, column=3, sticky="nsew")

# make a button to close the window
quit_button = tk.Button(root, text='Quit', 
                        bg='tan', command=root.destroy)
quit_button.grid(row=0, column=4, sticky="nsew")

# add skill buttons
for row in range(rows):
    for col in range(len(grid_list[row])):
        skillname=grid_list[row][col]
        image_name=job_skills[job_skills['skills']==skillname]['name'].tolist()[0]
        img = Image.open(image_name)
        img = img.resize((40,40), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        button_frame = tk.Frame(root, 
                 borderwidth=2, 
                 relief='ridge')
        button_frame.grid(column=col+1, row=row+2, sticky="nsew")
        button = tk.Button(button_frame, text=skillname,image=photo,
                           command= lambda x=skillname : rotation_list.append(x))
        button.grid(column=col, row=row, sticky="nsew")
        
        button.image = photo
        #button.grid(row=row, column=col, sticky="nsew")
        button.pack(fill='x')



if len(add_grid_list)>0:
    specialskill=tk.Label(root,text='Special')
    specialskill.grid(row=rows+3,column=1,sticky='nsew')
    for row2 in range(special_rows):
        for col2 in range(len(add_grid_list[row2])):
            skillname=add_grid_list[row2][col2]
            image_name=job_skills[job_skills['skills']==skillname]['name'].tolist()[0]
            img = Image.open(image_name)
            img = img.resize((40,40), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            button_frame = tk.Frame(root, 
                     borderwidth=2, 
                     relief='ridge')
            #button_frame.grid(column=0, row=0, sticky="nsew")
            button_frame.grid(column=col2+1, row=row2+rows+4, sticky="nsew")
            button = tk.Button(button_frame, text=skillname,image=photo,
                               command= lambda x=skillname : rotation_list.append(x))
            button.grid(column=col2, row=row2, sticky="nsew")
            
            button.image = photo
            #button.grid(row=row, column=col, sticky="nsew")
            button.pack(fill='x')
    

root.mainloop()


