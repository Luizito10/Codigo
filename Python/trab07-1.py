# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:16:37 2017

@author: viana
"""

import numpy as np
import matplotlib.pyplot as plt


#Definindo as Entradas e Saidas
entradas = np.array([71.0, 64.0, 43.0, 67.0, 56.0, 73.0, 68.0, 56.0, 76.0, 65.0, 45.0, 58.0, 45.0, 53.0, 49.0, 78.0, 73.0, 68.0])
saidas = np.array([82.0, 91.0, 100.0, 68.0, 87.0, 73.0, 78.0, 80.0, 65.0, 84.0, 116.0, 76.0, 97.0, 100.0, 105.0, 77.0, 73.0, 78.0])

#Fazendo as inicializações necessarias
alfa = 0.0001
want = (np.random.rand(1,1)) - 0.5
bant = (np.random.rand(1,1)) - 0.5
ciclos = 0
#Iniciando a condição de parada
A = -1.026665294

#Treinamento da rede
teste = len(entradas)
while ciclos < 100000:
    ciclos += 1
    for i in range(len(saidas)):
        y_entrada = want * entradas[i] + bant
        wnovo = want + alfa*(saidas[i]-y_entrada)*entradas[i]
        bnovo = bant + alfa*(saidas[i]-y_entrada)
        want = wnovo
        bant = bnovo

print(ciclos)
print(wnovo)
print(bnovo)

#Apos os treinamentos definiremos
a = float(wnovo)
b = float(bnovo)
print (a)
print (b)

#Criando a reta
horiz = []
vertic = []
teste = 0
x = 40.0
while(x < 80):
    teste = (a*x) + b
    horiz.append(x)
    vertic.append(teste)
    x += 0.1
    

#Mostrando no grafico
plt.plot((horiz),(vertic),'b-')
#Agora a geração do Gráfico
plt.plot((entradas),(saidas), 'r*')
plt.ylabel(u"Massa Muscular")
plt.xlabel(u"Idade")
plt.xlim(40.0,80.0)
plt.ylim(60.0,120.0)
plt.show()




















