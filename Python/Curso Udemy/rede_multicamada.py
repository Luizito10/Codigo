# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:26:15 2017

@author: Luiz Viana
"""

import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([[0], [1], [1], [0]])  #Saida XOR
pesos0 = np.random.rand(2,3)
pesos1 = np.random.rand(3,1)

def sigmoide(soma):
    return 1/(1+np.exp(-soma))

def sigmoideDerivada(sig):
    return sig * (1-sig)


#Definição da Qtdade de Ciclos
ciclos = 100000

for i in range(ciclos):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoide(somaSinapse0)
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoide(somaSinapse1)
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    
    

    