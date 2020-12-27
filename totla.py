# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:20:39 2020

@author: shshi

"""
# --- import ---
import tkinter as tk
import tkinter.messagebox
import pandas as pd
import os
import re
import math
from PIL import ImageTk, Image

# --- functions ---
def updateoptions(*args):
    jobs = job_dict[role_variable.get()]
    job_variable.set(jobs[0])
    menu = optionmenu_job['menu']
    menu.delete(0, 'end')
    for job in jobs:
        menu.add_command(label=job, command=lambda job_arg=job: job_variable.set(job_arg))

def submit2(rotation):
    window2=tk.Toplevel()
    window2.title("Join")
    window2.geometry("500x100")
    window2.configure(background="grey")
    window2.attributes("-alpha",0.5,"-topmost",True)
    print(rotation)
        
    
def submit(*args):
    var1 = role_variable.get()
    var2 = job_variable.get()
   # if tkinter.messagebox.askokcancel("Selection", "Confirm selection: " + var1 + ' ' + var2):
    chosen_job=abbreviation_dict[var2]
    grid_list, rows, add_grid_list, special_rows, role_list, role_rows=populate_grid(chosen_job)
    window = tk.Toplevel() 
    # create frame where buttons can be placed in
    window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], weight=1)
    window.columnconfigure([0,1,2,3,4,5,6,7,8,9], weight=1)
    rotation_list=list()

    # make a button to confirm the rotation
    confirm_button = tk.Button(window, text='confirm',
                            bg='azure',command= lambda l=rotation_list: submit2(l))
    
    confirm_button.grid(row=0, column=1, sticky="nsew")
    
    
    #make a button to remove the last skill added to the rotation list
    back_button = tk.Button(window, text='back',
                            bg='azure', command=rotation_list.pop)
    
    back_button.grid(row=0, column=2, sticky="nsew")
    
    # make a button to clear the rotation made
    clear_button = tk.Button(window, text='Clear',
                             bg='yellow', command= lambda l=rotation_list: pop_all(l))
    
    clear_button.grid(row=0, column=3, sticky="nsew")
    
    # make a button to close the window
    quit_button = tk.Button(window, text='other job', 
                            bg='tan', command=window.destroy)
    quit_button.grid(row=0, column=4, sticky="nsew")
    
    # make a button to change the job
    quit_button = tk.Button(window, text='Quit', 
                            bg='tan', command=root.destroy)
    quit_button.grid(row=0, column=5, sticky="nsew")
    
    
    classskill=tk.Label(window,text="Class skills")
    classskill.grid(row=1,column=1,sticky='nsew')
    # add skill buttons
    for row in range(rows):
        for col in range(len(grid_list[row])):
            skillname=grid_list[row][col]
            image_name=job_skills[job_skills['skills']==skillname]['name'].tolist()[0]
            img = Image.open(image_name)
            img = img.resize((40,40), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            button_frame = tk.Frame(window, 
                     borderwidth=2, 
                     relief='ridge')
            #button_frame.grid(column=0, row=0, sticky="nsew")
            button_frame.grid(column=col+1, row=row+2, sticky="nsew")
            button = tk.Button(button_frame, text=skillname,image=photo,
                               command= lambda x=skillname : rotation_list.append(x))
            button.grid(column=col, row=row, sticky="nsew")
            
            button.image = photo
            #button.grid(row=row, column=col, sticky="nsew")
            button.pack(fill='x')
            
    if len(add_grid_list)>0:
        specialskill=tk.Label(window,text='Special')
        specialskill.grid(row=rows+3,column=1,sticky='nsew')
        for row2 in range(special_rows):
            for col2 in range(len(add_grid_list[row2])):
                skillname=add_grid_list[row2][col2]
                image_name=job_skills[job_skills['skills']==skillname]['name'].tolist()[0]
                img = Image.open(image_name)
                img = img.resize((40,40), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                button_frame = tk.Frame(window, 
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
    else:
        special_rows=0
                
    # add role actions
    roleskill=tk.Label(window,text='Role actions')
    roleskill.grid(row=rows+special_rows+3,column=1,sticky='nsew')
    for row3 in range(role_rows):
        for col3 in range(len(role_list[row3])):
            skillname=role_list[row3][col3]
            image_name=job_skills[job_skills['skills']==skillname]['name'].tolist()[0]
            img = Image.open(image_name)
            img = img.resize((40,40), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            button_frame = tk.Frame(window, 
                     borderwidth=2, 
                     relief='ridge')
            #button_frame.grid(column=0, row=0, sticky="nsew")
            button_frame.grid(column=col3+1, row=row3+rows+special_rows+6, sticky="nsew")
            button = tk.Button(button_frame, text=skillname,image=photo,
                               command= lambda x=skillname : rotation_list.append(x))
            button.grid(column=col3, row=row3, sticky="nsew")
            
            button.image = photo
            #button.grid(row=row, column=col, sticky="nsew")
            button.pack(fill='x')
                
    return rotation_list

# disassemble filename
def split_filename(filename):
    return re.split('[\\\. ]',filename)


# Empty a list
def pop_all(l):
    r, l[:] = l[:], []
    return r

# devide rows and columns
def grid_make(skill_list,n):
    grid_list=list()
    rows=math.ceil(len(skill_list)/n)
    for i in range(rows):
        grid_list.append(skill_list[:n].tolist())
        skill_list=skill_list[n:]
    return grid_list, rows


# make a grid
def populate_grid(job):

    chosen_job=job_skills[job_skills['job']==job]
    special_list=chosen_job[~chosen_job['special skill'].isnull()]['skills']
    skill_list=chosen_job[chosen_job['special skill'].isnull()]['skills']
    role=role_action_dict[list(set(chosen_job['job_function']))[0]]
    role_skill_list=job_skills[job_skills['job']==role]['skills']
    
    grid_list, rows=grid_make(skill_list,8)
    special_grid_list, special_rows=grid_make(special_list,8)
    role_grid_list, role_rows=grid_make(role_skill_list,8)

    return grid_list, rows, special_grid_list, special_rows, role_grid_list, role_rows


# -------------------------------------------
    
path='ffxiv_dps_rotation_simul\\skill_icons'
files = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith(('.png','jpeg'))]
job_skills=pd.read_excel('ffxivjob.xlsx')


# necessary dictionaries

job_dict={'Tank':['Paladin','Warrior','Dark Knight','Gunbreaker'],
          'Heal':['White Mage','Scholar','Astrologian'],
          'Melee':['Monk','Dragoon','Ninja','Samurai'],
          'Ranged':['Bard','Machinist','Dancer'],
          'Magic':['Black Mage','Summoner','Red Mage'] }

abbreviation_dict={'Paladin':'pld','Warrior':'war','Dark Knight':'drk','Gunbreaker':'gnb',
                   'White Mage':'whm','Scholar':'sch','Astrologian':'ast',
                   'Bard':'brd','Machinist':'mch','Dancer':'dnc',
                   'Monk':'mnk','Dragoon':'drg','Ninja':'nin','Samurai':'sam',
                   'Black Mage':'blm','Summoner':'smn','Red Mage':'rdm'
    }

role_action_dict={'heal':'HealerRollAction',
                  'magic':'MagicalRangedRollAction',
                  'melee':'MeleeRollAction',
                  'ranged':'PhysicalRangedRollAction',
                  'tank':'TankRollAction'}

root=tk.Tk()



# Create option menus to choose 
role_variable=tk.StringVar()
job_variable=tk.StringVar()

role_variable.trace('w', updateoptions)
optionmenu_role = tk.OptionMenu(root, role_variable, *job_dict.keys())
optionmenu_job = tk.OptionMenu(root, job_variable, '')

role_variable.set('Tank')
optionmenu_role.pack()
optionmenu_job.pack()

btn=tk.Button(root, text='Submit', width=8, command=submit)
btn.pack()

root.mainloop()