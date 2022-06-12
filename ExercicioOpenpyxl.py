# -*- coding: utf-8 -*-
"""
Created on Wed May 11 18:00:34 2022

@author: Edgar Alexander

Criar uma planilha em Excel a partir do Python contendo:
• Nome do Aluno, Nota 1, Nota 2, Nota 3, Média (calculada)
• A média é ponderada e a maior nota tem peso 3 e as demais tem peso 2.

• Fazer uma função para:
• Mostrar na tela os alunos aprovados e os alunos reprovados
• Aprovados >= 6.0
• Reprovados < 6.0
• Fazer um gráfico de pizza com o percentual de alunos aprovados e os
reprovados.
"""
from openpyxl import Workbook

class Aluno:
    
    def __init__(self,nome="",nota1=0.0,nota2=0.0,nota3=0.0):
        self.nome  = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = self.calcula_media(nota1, nota2, nota3)
        self.status = self.verifica_aprovacao(self.media)
        
    def calcula_media(self,n1,n2,n3):
        if (n1>=n2) and (n1>=n2):
            soma = 3*n1 + 2*n2 + 2*n3
        elif (n2>=n1) and (n2>=n3):
            soma = 3*n2 + 2*n1 + 2*n3
        else:
            soma = 3*n3+2*n2 + 2*n1
        return (soma / 7)
    
    def verifica_aprovacao(self,media):
        if media >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"
    def to_list(self):
        return [self.nome, self.nota1, self.nota2, self.nota3, self.media, self.status]
        
class Alunos:
    
    def __init__(self, lista_alunos=[]):
        self.alunos = lista_alunos.copy()
        
    def insere(self,aluno):
        self.alunos.append(aluno)
        
    def __str__(self):

        txt = "["
        for aluno in self.alunos:
            txt = txt + aluno.nome +", " + str(aluno.nota1)+", "\
                    + str(aluno.nota2)+", "+ \
                    str(aluno.nota3)+", " + \
                    str(aluno.media)+", " + \
                    aluno.status+","
        txt = txt + "]"
        return txt
    
    def salva_excel(self, nome_workbook="Alunos.xlsx", nome_planilha="planilha1", cabecalho=[], celula_inicial="A1"):
        arquivo_excel = Workbook()
        planilha1 = arquivo_excel.active
        planilha1.title = nome_planilha
        planilha1.append(cabecalho)
        for aluno in self.alunos:
            planilha1.append(aluno.to_list())
        arquivo_excel.save(nome_workbook)
            

#cabecalho = ["Nome","Nota1","Nota2","Nota3","Media","Situação"]
#aluno1 = Aluno("Edgar Alexander", 10.0, 8.5, 9.7)
#aluno2 = Aluno("João da Silva Neto", 7.0, 6.5, 9.5)
#aluno3 = Aluno("Pedro Andre", 7.5, 3.5, 1.5)
#aluno4 = Aluno("Ana Paula Torres", 7.3, 3.5, 3.5)
#alunos = Alunos()
#alunos.insere(aluno1)
#alunos.insere(aluno2)
#alunos.insere(aluno3)
#alunos.insere(aluno4)
#alunos.salva_excel("Alunos_teste.xlsx", "Alunos",cabecalho,"A1")
#print(alunos)