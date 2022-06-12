# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:12:15 2022

@author: edgar alexander
"""

from math import *
import matplotlib.pyplot as plt

class Ponto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def copy(self):
        ponto = Ponto(self.x, self.y)
        return ponto
        
    def __sub__(self, other):
        result = Ponto()
        result.x = other.x - self.x
        result.y = other.y - self.y
        return result
    
    def __str__(self):
        texto = "(" + str(self.x) + ", "+ str(self.y) +")"
        return texto
        
class Vetor:
    
    def __init__(self, p1=0, p2=0, modulo=0, angulo=0):
        if p1!=0 and p2!=0:
            self.p1 = p1
            self.p2 = p2
            self.v = p1 - p2
            self.Vx = Ponto(self.v.x,0)
            self.Vy = Ponto(0,self.v.y)
            self.modulo = sqrt(self.v.x**2 + self.v.y**2)
            self.angulox =degrees(acos((self.Vx.x*self.v.x + self.Vx.y*self.v.y)/(sqrt(((self.v.x**2)+(self.v.y**2)))*sqrt((self.Vx.x**2)+(self.Vx.y**2)))))
            self.anguloy =degrees(acos((self.Vy.x*self.v.x + self.Vy.y*self.v.y)/(sqrt(((self.v.x**2)+(self.v.y**2)))*sqrt((self.Vy.x**2)+(self.Vy.y**2)))))
        elif modulo!=0:
            self.modulo  = modulo
            self.angulox = angulo
            self.v = Ponto(modulo*(cos(radians(angulo))), modulo*(sin(radians(angulo)))) 
            self.Vx = Ponto(self.v.x,0)
            self.Vy = Ponto(0,self.v.y) 
            self.p1 = Ponto(0,0)
            self.p2 = self.v.copy()
            self.anguloy = degrees(acos((self.Vy.x*self.v.x + self.Vy.y*self.v.y)/(sqrt(((self.v.x**2)+(self.v.y**2)))*sqrt((self.Vy.x**2)+(self.Vy.y**2)))))
        else:
            print("Erro na entrada de dados!!!")
    def __str__(self):
        texto = "(" + str(self.v.x) + ", "+ str(self.v.y) +")"
        return texto

    
    def norma(self):
        """ norma do vetor - corresponde a seu comprimento. |v|"""
        return sqrt(self.v.x**2 + self.v.y**2)
        
    def produto_interno(self, other):
        """ Considerando dois vetores v = (a,b) e u = (a',b'),
            o produto interno entre eles é denotado por <v,u> e é dado pela 
            seguinte expressão:
                    <v,u> = a·a' + b·b'  """
        return (self.v.x * other.v.x) + (self.v.y * other.v.y)
        
    def __add__(self, other):
        rx,ry = (self.v.x + other.v.x, self.v.y + other.v.y)
        p1 = Ponto(0,0)
        p2 = Ponto(rx,ry)
        vet_soma = Vetor(p1,p2)
        return vet_soma
    
    def __sub__(self, other):
        rx,ry = (self.v.x - other.v.x, self.v.y - other.v.y)
        p1 = Ponto(0,0)
        p2 = Ponto(rx,ry)
        vet_soma = Vetor(p1,p2)
        return vet_soma

class Vetdesign:
    
    def __init__(self, vetores=[], cores=[], tamanho=(20,25), titulo = "", nome_eixoX="", nome_eixoY=""):
        
        self.vetores = vetores
        self.cores = cores
        self.tamanho = tamanho
        self.titulo = titulo 
        self.nome_eixoX = nome_eixoX
        self.nome_eixoY = nome_eixoY
        
    def show(self):
        
        plt.figure(figsize = self.tamanho, constrained_layout=True)
      
        self.ax = plt.axes()
        for vet in self.vetores:
            self.ax.arrow(0, 0, vet.v.x, vet.v.y, head_width=0.05, head_length=0.1, fc='k', ec='k')
        plt.show()
        
        