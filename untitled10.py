# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:57:30 2022

@author: edgar
"""
import tkinter as tk
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Cria a variável de aplicação.
        self.contents = tk.StringVar()
        # Coloca algum valor na variável.
        self.contents.set("Esta é uma variavel")
        # informa o entry widget para monitorar a variável.
        self.entrythingy["textvariable"] = self.contents

        # Define o callback para quando o usuário clicar em return.
        # Será impresso o valor da variável.
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("Olá, o valor atual inserido na caixa de texto é:", self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()