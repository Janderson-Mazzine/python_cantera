# -*- coding: utf-8 -*-

"""
Codigo para determinação da velocidade de queima de uma chama pré misturada
para diferentes temperaturas e razões de equivalência. Combustível Etanol
(C2H5OH)
"""

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros de entrada
p = 8*ct.one_atm  # Pressão de 8 atm
tpoints = 7
Tin = np.linspace(300, 600, tpoints) #Em Kelvin
gas = ct.Solution('c2c3.cti')

width = 0.03  # Em metros

for j in range(tpoints): #Varia a temperatura de entrada
    npoints=50
    phi = np.linspace(0.35, 3.00, npoints)
    vms = []
    vin = []
    for i in range(npoints): #Varia o phi
        gas.X = {'C2H5OH':1, 'O2':3/phi[i], 'N2':3*3.76/phi[i]} #Seta a relação ar combustível
        gas.TPX = Tin[j], p, gas.X
        leg= str(int(Tin[j]))+" K"
        
        # Calculo da chama
        f = ct.FreeFlame(gas, width=width)
        f.set_refine_criteria(ratio=3, slope=0.07, curve=0.14)
        f.solve(loglevel=0, auto=True) #loglevel=0 caso não queira visualizar as etapas no console
        
        #Preenche os vetores velocidade
        vms.append(f.u[0])
        vin.append(f.u[0]*39.3701)
        
        #Visualizar resultados
        print('Razão de Equivalencia = ' + str(phi[i]))
        print('Temperatura de entrada = ' + str(Tin[j]))
        print('\nVelocidade de chama = {:7f} m/s\n'.format(f.u[0]))
        print('\nVelocidade de chama = {:7f} in/s\n'.format(f.u[0]*39,3701))
        
    #Plotar e salvar gráfico Velocidade de chama x Razão de equivalência, em m/s
    plt.figure(1)
    plt.plot(phi, vms, label=leg)
    plt.suptitle("Velocidade de chama em m/s x Razão de equivalência",fontsize=14)
    plt.title('Combustível Etanol (C2H5OH)',fontsize=11)
    plt.legend()
    plt.xlabel('Razão de Equivalência')
    plt.ylabel('Velocidade [m/s]')
    plt.savefig("v_ms_etanol.png")
 
    #Plotar e salvar gráfico Velocidade de chama x Razão de equivalência, em in/s        
    plt.figure(2)
    plt.plot(phi, vin, label=leg)
    plt.suptitle("Velocidade de chama em in/s x Razão de equivalência",fontsize=14)
    plt.title('Combustível Etanol (C2H5OH)',fontsize=11)
    plt.legend()
    plt.xlabel('Razão de Equivalência')
    plt.ylabel('Velocidade [in/s]')
    plt.savefig("v_ins_etanol.png")

#Visualizar Gráficos
plt.show(1)
plt.show(2)