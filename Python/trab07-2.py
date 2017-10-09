# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 20:41:51 2017

@author: viana
"""

import numpy as np
import matplotlib.pyplot as plt

#Definindo as Entradas e Saidas
entradas = np.array([3, 5, 10, 10, 20, 20, 20, 30, 40, 50, 60, 70, 70, 80, 100, 100, 100, 120, 120, 140, 150, 180, 180, 200, 200])
saidas = np.array([1.5, 2.0, 6.0, 7.0, 10.0, 12.0, 15.0, 8.0, 10.0, 20.0, 20.0, 25.0, 30.0, 25.0, 40.0, 35.0, 40.0, 30.0, 40.0, 40.0, 50.0, 40.0, 50.0, 60.0, 50.0])

#Fazendo as inicializações necessarias
alfa = 0.0001
want = (np.random.rand(1,1)) - 0.5
bant = (np.random.rand(1,1)) - 0.5
ciclos = 0


#Treinamento da rede
teste = len(entradas)
while ciclos < 10:
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
x = 0
while(x < 200):
    teste = (a*x) + b
    horiz.append(x)
    vertic.append(teste)
    x += 0.1
    

#Mostrando no grafico
plt.plot((horiz),(vertic),'b-')
#Agora a geração do Gráfico
plt.plot((entradas),(saidas), 'r*')
plt.ylabel(u"Gasto com Alimentação")
plt.xlabel(u"Renda Familiar")
plt.xlim(0.0,200.0)
plt.ylim(0.0,65.0)
plt.show()
