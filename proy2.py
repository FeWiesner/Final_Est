import csv
with open('datos.csv', encoding = 'UTF-8') as csv_file:
    read = csv.reader(csv_file, delimiter=',')
    i = 0
    d = {}
    for row in read:
        if i == 0:
            header = row
        else:
            d[i] = []
            for j in row:
                if j == '0':
                    del (d[i])
                    break
                elif j == 'a' or j == 'b':
                    d[i].append(j)
                else:
                    d[i].append(round(float(j),3))
            
        i += 1

import numpy as np
import scipy.stats as ss
'''
['Genero', 'Primero', 'Segundo', 'Tercero', 'Final', 'Complementaria', 'Nota Curso']
'''
import matplotlib.pyplot as plt

l1 = ['Primero', 'Segundo', 'Tercero', 'Final', 'Complementaria', 'Nota Curso']
lista = []

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

for i in d:
    lista.append(d[i][1])
lista.sort()

Y = np.asarray(lista) #estadisticos de orden

A = []
for i in lista:
    suma = sum(Y <= i) #se van contando los estadisticos menores a un valor
    A.append(suma/len(lista)) #se normaliza
ECD = np.asarray(A) #distribucion empirica acumulada

x = np.linspace(0,5,50) #pasos uniformes para sacar la normal acumulada
y = ss.norm.cdf(x, loc = 3, scale = 1) #normal acumulada media mu, desviacion sigma
test=ss.ks_2samp(ECD, y) #test de KS, retorna estadistico y p-valor
print(test)
#Ejemplo: KstestResult(statistic=0.26, pvalue=0.06779471096995852)

plt.hist(lista, cumulative= True, density = True, bins = 50) #histograma de la empirica acumulada
plt.plot(x, y )#grafico de la normal
plt.plot(Y, ECD) #grafico del muestreo
plt.show()


Mtest = np.empty([10,10])

i = 0
j = 0
for mu in range(0,50, 5):
    for sig in range(0,50, 5):
        y = ss.norm.cdf(x, loc = mu/10, scale = sig/10)
        test=ss.ks_2samp(ECD, y)
        Mtest[i][j] = test[1]
        j+=1
    j = 0
    i+=1

acepta = []
for i in range(10):
    for j in range(10):
        if Mtest[i][j] >= 0.05:
            acepta.append((i/2, j/2))
print(acepta)



        

