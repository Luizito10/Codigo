# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:49:58 2017

@author: Luiz Viana
"""
#Perceptron para "E e OU"
import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0, 0, 0, 1])  #Saida AND
saidas = np.array([0, 1, 1, 1]) #Saida OR
pesos = np.array([0.0,0.0])
alfa = 0.1 #Taxa de Aprendizagem

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)
 
def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (alfa*entradas[i][j]*erro)
                print("Peso atualizado "+str(pesos[j]))
        print("Total de Erros: " + str(erroTotal))
        
treinar()
print("Rede neural Treinada")
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))









