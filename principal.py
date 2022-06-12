# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:03:02 2022

@author: edgar
"""

from vetpy import Ponto
from vetpy import Vetor
from vetpy import Vetdesign

A = Vetor(modulo=10,angulo=60)
B = Vetor(modulo=8, angulo=360)
C = A + B
print("O modulo dos vetores é : ", C.modulo)

v0 = Ponto(3,3)
v1 = Ponto(5,5)
u0 = Ponto(0,0)
u1 = Ponto(3,5)

v = Vetor(v0,v1)
u = Vetor(u0,u1)

print(v.v)
print("norma: ",v.norma())
print("Angulo x:",v.angulox)
print("Angulo y:",v.anguloy)
produto = v.produto_interno(u)
print(produto)

x = v + u
print(x.v)

projetil = Vetor(modulo=20,angulo=60)
print("Projetil ",projetil.v)
print("Exercício projetil, angulo: ",projetil.anguloy)

F1 = Vetor(modulo=6, angulo=91)
F2 = Vetor(modulo=8, angulo=1)
F3 = F1 + F2
print(F3.modulo)


F4 = Vetor(modulo=30, angulo=180)
F5 = Vetor(modulo=20, angulo=60)
F6 = Vetor(modulo=10, angulo=270)
F7 = F4 + F5 + F6
print(F7.modulo)

va = Vetor(modulo=5, angulo=30)
vb = Vetor(modulo=12, angulo=75)
vc = va + vb
print(vc.modulo)

pontos = [va,vb,va+vb]
vd = Vetdesign(pontos)
vd.show()