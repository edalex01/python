# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:07:57 2022

@author: edgar
"""

from tkinter import Frame
from tkinter import Label
from tkinter import Tk

class Application:
 def __init__(self, master=None):
      self.widget1 = Frame(master)
      self.widget1.pack()
      self.msg = Label(self.widget1, text="Primeiro widget")
      self.msg.pack ()
root = Tk()
Application(root)
root.mainloop()