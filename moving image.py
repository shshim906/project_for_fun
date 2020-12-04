# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:50:07 2020

@author: shshi
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:29:55 2020

@author: shshi
"""


import tkinter as tk
from PIL import ImageTk, Image

# --- functions ---

def move_b():
    canvas.move(b, 1, 0)
    canvas.move(c, 1, 0)
    # move again after 25ms (0.025s)
    root.after(25, move_b)
    
# def move_c():
#     canvas.move(c, 1, 0)
#     # move again after 25ms (0.025s)
#     root.after(10, move_c)

# --- main ---

# init
root = tk.Tk()
root.title("Join")
root.geometry("800x150")
root.configure(background='white')
path='aero.png'

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
orig_img=Image.open(path)
orig_img=orig_img.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(orig_img)

# create frame
frame=tk.Frame(root)
frame.pack()

# create canvas
canvas = tk.Canvas(root, width=1000, height=100)
canvas.pack()

# create object
#b = canvas.create_rectangle(0, 0, 100, 100, fill='blue')
b = canvas.create_image(-50, 100, anchor='sw', image=img)
gcd = canvas.create_rectangle(350, 0, 400, 100)

# create button
start_b=tk.Button(frame, 
                  text="Start",
                  command=move_b)
start_b.pack(side=tk.LEFT)

quit_b=tk.Button(frame, 
                 text="Quit",
                 fg="red",
                 command = root.destroy)
quit_b.pack(side=tk.LEFT)


c = canvas.create_image(0, 50, anchor='sw', image=img)
# start moving `gcd` and 'ogcd' automatically
#move_b()
#move_c()
# start program
root.mainloop()