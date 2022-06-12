# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:24:44 2022

@author: edgar
"""

#!/usr/bin/env python 
import tkinter as tk 

class Application(tk.Frame): 
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W) 
        self.createWidgets()

    def createWidgets(self):
        top=self.winfo_toplevel()          # Janela principal
        top.minsize(width=800, height=600) # Tamanho mínimo da janela
        #top.rowconfigure(0, weight=1)
        #top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.fonte = ('Arial', 12)
        
# ----------- Frame de Cadastro de Alunos ------------------------------------
        self.LF_incluir = tk.LabelFrame(top, labelanchor='nw',text=' Cadastro de Alunos ',font = self.fonte)
        self.LF_incluir.grid(row=0, column=0,columnspan=8, padx=30, pady=30, ipadx=10, ipady=10 )

# ---------  Entrada de Dados do nome do aluno -------------------------------        
        self.LB_nome = tk.Label(self.LF_incluir, text='Nome do Aluno: ', font = self.fonte)
        self.LB_nome.grid(row=0,column=0)
        self.E_nome = tk.Entry(self.LF_incluir, width=30, font = self.fonte)
        self.E_nome.grid(row=0,column=1, padx=10, pady=10)

# ----------- Entrada de Dados da Nota 1 do aluno ---------------------------
        self.LB_nota1 = tk.Label(self.LF_incluir, text='Nota 1: ', font = self.fonte)
        self.LB_nota1.grid(row=0,column=3)
        self.E_nota1 = tk.Entry(self.LF_incluir, width=4, font = self.fonte)
        self.E_nota1.grid(row=0,column=4, padx=10, pady=10)
                
# ----------- Entrada de Dados da Nota 2 do aluno ---------------------------
        self.LB_nota2 = tk.Label(self.LF_incluir, text='Nota 2: ',font = self.fonte)
        self.LB_nota2.grid(row=0,column=5)
        self.E_nota2 = tk.Entry(self.LF_incluir, width=4, font = self.fonte)
        self.E_nota2.grid(row=0,column=6, padx=10, pady=10)
                 
# ----------- Entrada de Dados da Nota 3 do aluno ---------------------------
        self.LB_nota3 = tk.Label(self.LF_incluir, text='Nota 3: ',font = self.fonte)
        self.LB_nota3.grid(row=0,column=7)
        self.E_nota3 = tk.Entry(self.LF_incluir, width=4, font = self.fonte)
        self.E_nota3.grid(row=0,column=8, padx=10, pady=10)
        
# ----------- Botão Incluir -------------------------------------------------       
        self.BT_incluir = tk.Button(self.LF_incluir, width = 15, text='Incluir', font = self.fonte, command=incluir)
        self.BT_incluir.grid(row=1, column=7, columnspan=2, sticky=tk.E+tk.S) 

# ----------- Frame Alunos Cadastrados ------------------------------------
        self.LF_tabela = tk.LabelFrame(top, labelanchor='nw',text=' Alunos Cadastrados ',font = self.fonte)
        self.LF_tabela.grid(row=2, column=0,columnspan=8, padx=30, pady=30, ipadx=10, ipady=10 )
        
#------------- Tabela ------------------------------------------------------

#-------------- Cabeçalho da Tabela ----------------------------------------
        self.LB_tabnome = tk.Label(self.LF_tabela, text='Nome ', width = 35, font = self.fonte)
        self.LB_tabnome.grid(row=0, column=0, sticky=tk.E+tk.W)
 
        self.LB_tabnota1 = tk.Label(self.LF_tabela, text='Nota 1 ', width = 10, font = self.fonte)
        self.LB_tabnota1.grid(row=0, column=1, sticky=tk.E+tk.W)
        
        self.LB_tabnota2 = tk.Label(self.LF_tabela, text='Nota 2 ', width = 10, font = self.fonte)
        self.LB_tabnota2.grid(row=0, column=2, sticky=tk.E+tk.W)
        
        self.LB_tabnota3 = tk.Label(self.LF_tabela, text='Nota 3 ', width = 10, font = self.fonte)
        self.LB_tabnota3.grid(row=0, column=3, sticky=tk.E+tk.W)
        
        self.LB_tabmedia = tk.Label(self.LF_tabela, text='Média ', width = 10, font = self.fonte)
        self.LB_tabmedia.grid(row=0, column=4, sticky=tk.E+tk.W)
        
        self.LB_tabsituacao = tk.Label(self.LF_tabela, text='Situação ', width = 20, font = self.fonte)
        self.LB_tabsituacao.grid(row=0, column=5, sticky=tk.E+tk.W)
        
        self.E_tabnome     = dict()
        self.E_tabnota1    = dict()
        self.E_tabnota2    = dict()
        self.E_tabnota3    = dict()
        self.E_tabmedia    = dict()
        self.E_tabsituacao = dict() 
        
        for i in range(1,11):
           
            self.E_tabnome[i] = tk.Entry(self.LF_tabela, width = 35, font = self.fonte)
            self.E_tabnome[i].grid(row=i, column=0, sticky=tk.E+tk.W)
     
            self.E_tabnota1[i] = tk.Entry(self.LF_tabela, width = 10, font = self.fonte)
            self.E_tabnota1[i].grid(row=i, column=1, sticky=tk.E+tk.W)
            
            self.E_tabnota2[i] = tk.Entry(self.LF_tabela,  width = 10, font = self.fonte)
            self.E_tabnota2[i].grid(row=i, column=2, sticky=tk.E+tk.W)
            
            self.E_tabnota3[i] = tk.Entry(self.LF_tabela,  width = 10, font = self.fonte)
            self.E_tabnota3[i].grid(row=i, column=3, sticky=tk.E+tk.W)
            
            self.E_tabmedia[i] = tk.Entry(self.LF_tabela, width = 10, font = self.fonte)
            self.E_tabmedia[i].grid(row=i, column=4, sticky=tk.E+tk.W)
            
            self.E_tabsituacao[i] = tk.Entry(self.LF_tabela, width = 20, font = self.fonte)
            self.E_tabsituacao[i].grid(row=i, column=5, sticky=tk.E+tk.W)
            
# ----------- Botão Excluir -------------------------------------------------       
        self.BT_incluir = tk.Button(self.LF_tabela, width = 15, text='Excluir', font = self.fonte, command=incluir)
        self.BT_incluir.grid(row=i+1, column=5, columnspan=2, sticky=tk.E+tk.S) 

            



#------------------------------- Botões Exportar Excel e Sair -----------------------------------------
# ----------- Frame para Botões Finais ------------------------------------
        self.F_final = tk.Frame(top)
        self.F_final.grid(row=3, column=0, padx=30, pady=30, ipadx=10, ipady=10 )

#------------------------------  Botões -----------------------------------
        self.BT_exportar = tk.Button(self.F_final, width = 15, text='Exportar Excel', font = self.fonte, command=incluir)
        self.BT_exportar.grid(row=0, column=0, columnspan=2, sticky=tk.W) 

        self.BT_sair = tk.Button(self.F_final, width = 15, text='Sair', font = self.fonte, command=sair)
        self.BT_sair.grid(row=0, column=6, columnspan=2, sticky=tk.E) 



def incluir():
    pass

def sair():
    pass

def importar():
    pass

app = Application() 
app.master.title('FISBACH SYSTEM  version.2022.0.1')
app.mainloop()