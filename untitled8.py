# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:21:08 2022

@author: edgar
"""

from tkinter import Tk, mainloop, TOP, BOTTOM
from tkinter.ttk import Button 
from time import time 
root = Tk() 
  
button = Button(root, text = 'Geeks') 
button.pack(side = BOTTOM, padx=100) 
  
print('Running...') 
start = time() 
  
#root.after(5000, root.destroy) 
  
mainloop() 
end = time() 
print('Destroyed after % d seconds' % (end-start)) 