# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:24:44 2022

@author: edgar
"""

#!/usr/bin/env python 
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import ExercicioOpenpyxl as eop
import os

class Application(tk.Frame): 
    def __init__(self, master=None):
        self.alunos = eop.Alunos()
        tk.Frame.__init__(self, master)
        self.S_exclui = dict()  # variavel do checkbutton para marcar exclusão de linha
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W) 
        self.createWidgets()
        self.E_nome.focus() # joga o foco para o primeiro campo
        
        
        

    def createWidgets(self):
        top=self.winfo_toplevel()          # Janela principal
        top.minsize(width=1200, height=650) # Tamanho mínimo da janela
        #top.rowconfigure(0, weight=1)
        #top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.fonte = ('Arial', 12)
        
        for i in range(1,11): # Cria as variáveis usadas em cada linha no checkbutton
            self.S_exclui[i] = tk.StringVar()
        
# ----------- Frame de Cadastro de Alunos ------------------------------------
        self.LF_incluir = tk.LabelFrame(top, labelanchor='nw',text=' Cadastro de Alunos ',font = self.fonte)
        self.LF_incluir.grid(row=0, column=0,columnspan=8, padx=120, pady=30, ipadx=50, ipady=10,sticky=tk.E )
        self.LF_incluir.columnconfigure(0, weight=1) # Transformar a coluna em esticável
        self.LF_incluir.columnconfigure(1, weight=1)
        self.LF_incluir.columnconfigure(2, weight=1)
        self.LF_incluir.columnconfigure(3, weight=1)
        self.LF_incluir.columnconfigure(4, weight=1)
        self.LF_incluir.columnconfigure(5, weight=1)
        self.LF_incluir.columnconfigure(6, weight=1)
        self.LF_incluir.columnconfigure(7, weight=1)
        self.LF_incluir.columnconfigure(8, weight=1)

# ---------  Entrada de Dados do nome do aluno -------------------------------        
        self.LB_nome = tk.Label(self.LF_incluir, text='Nome do Aluno: ', font = self.fonte)
        self.LB_nome.grid(row=0,column=0,padx=15)
        self.E_nome = tk.Entry(self.LF_incluir, width=30, font = self.fonte)
        self.E_nome.grid(row=0,column=1, padx=10, pady=10,sticky = tk.E)
        
        

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
        self.BT_incluir = tk.Button(self.LF_incluir, width = 15, text='Incluir', font = self.fonte, command=self.incluir)
        self.BT_incluir.grid(row=1, column=7, columnspan=2, sticky=tk.SW) 

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
        self.CB_excluir    = dict()
        
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
            
            self.CB_excluir[i] = ttk.Checkbutton(self.LF_tabela, 
                                                 variable= self.S_exclui[i], 
                                                 onvalue='exclui', 
                                                 offvalue='não exclui')
            self.CB_excluir[i].grid(row=i, column=6, padx=10, sticky=tk.E+tk.W)
            
            
# ----------- Botão Excluir -------------------------------------------------       
        self.BT_incluir = tk.Button(self.LF_tabela, width = 15, text='Excluir', font = self.fonte, command=self.excluir)
        self.BT_incluir.grid(row=i+1, column=5, columnspan=2, pady=10, sticky=tk.S+tk.W+tk.E+tk.N) 

            



#------------------------------- Botões Exportar Excel e Sair -----------------------------------------
# ----------- Frame para Botões Finais ------------------------------------
        self.F_final = tk.Frame(top)
        self.F_final.grid(row=3, column=0, padx=80,ipadx=20 )
        self.F_final.columnconfigure(1, weight=1)
        self.F_final.columnconfigure(2, weight=1)


#------------------------------  Botões -----------------------------------
        self.BT_exportar = tk.Button(self.F_final, width = 15, text='Exportar Excel', font = self.fonte, command=self.exportar)
        self.BT_exportar.grid(row=0, column=0,  sticky=tk.W) 

        self.BT_sair = tk.Button(self.F_final, width = 15, text='Sair', font = self.fonte, command=self.sair)
        self.BT_sair.grid(row=0, column=1,  sticky=tk.E) 
        



    def incluir(self):
        if (self.E_nome.get() == "") or (self.E_nota1.get()== "") or (self.E_nota2.get()=="") or (self.E_nota1.get()==""):
            messagebox.showerror("Erro","Não pode haver campo vazio, digite o nome, a nota 1, a nota 2 e a nota 3 e tecle inserir.")
        elif (self.E_nota1.get().isdigit() != True) or (float(self.E_nota1.get()) < 0.0) or (float(self.E_nota1.get())>10.0):
            messagebox.showerror("Erro","A nota 1 deve ser um dígito de 1.0 até 10.0. Tente novamente.")
        elif (self.E_nota2.get().isdigit() != True) or (float(self.E_nota2.get()) < 0.0) or (float(self.E_nota2.get())>10.0):
            messagebox.showerror("Erro","A nota 2 deve ser um dígito de 1.0 até 10.0. Tente novamente.")
        elif (self.E_nota3.get().isdigit() != True) or (float(self.E_nota3.get()) < 0.0) or (float(self.E_nota3.get())>10.0):
            messagebox.showerror("Erro","A nota 3 deve ser um dígito de 1.0 até 10.0. Tente novamente.")
            

        else:
            #----------- insere o aluno digitado na interface no objeto aluno ----------------
           aluno = eop.Aluno(nome=self.E_nome.get(), nota1=float(self.E_nota1.get()), nota2=float(self.E_nota2.get()), nota3=float(self.E_nota3.get()))
           self.alunos.insere(aluno)  # insere em alunos o conteudo do aluno incluido 
           i = 0
           #------- Limpa toda a tabela -----------
           for j in range(1,11):
               
               self.E_tabnome [j].delete ( 0, 30 )
               self.E_tabnota1[j].delete ( 0, 30 )
               self.E_tabnota2[j].delete ( 0, 30 )
               self.E_tabnota3[j].delete ( 0, 30 )
               self.E_tabmedia[j].delete ( 0, 30 )
               self.E_tabsituacao[j].delete ( 0, 30 )
           
           #-------- Insere na tabela o conteudo de alunos ------------------------
           for aluno in self.alunos.alunos:
               i+=1
               self.E_tabnome[i].insert(0,aluno.nome)
               self.E_tabnota1[i].insert(0,aluno.nota1)
               self.E_tabnota2[i].insert(0,aluno.nota2)
               self.E_tabnota3[i].insert(0,aluno.nota3)
               self.E_tabmedia[i].insert(0,"{: .1f}".format(float(aluno.media)))
               self.E_tabsituacao[i].insert(0,aluno.status)
               
           #-------- Limpa os campos de incluir aluno -------------
           self.E_nome.delete(0,30)
           self.E_nota1.delete(0,30)
           self.E_nota2.delete(0,30)
           self.E_nota3.delete(0,30)
           self.E_nome.focus()
          
       
    
    def sair(self):
        os._exit(0)
    
    def exportar(self):
        self.alunos.salva_excel(nome_workbook="situacao_alunos.xlsx", 
                        nome_planilha="Notas", 
                        cabecalho=["Nome","Nota1","Nota2","Nota3","Media","Situação"], 
                        celula_inicial="A1")
    
    def excluir(self):
        pass

app = Application() 
app.master.title('FISBACH SYSTEM  version.2022.0.1')
app.mainloop()