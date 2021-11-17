# -*- coding: utf-8 -*-
"""
Temperatura de chama adiabática em função da razão de equivalencia para
temperaturas de entrada no combustor de 300K a 1000K com uma pressão de
1,4 MPa e frações molares de CO2, CO, NO e NO2 em função da razão de 
equivalência, para o combustível PROPANO (C3H8).
"""

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

#Estilo de gráfico
#plt.style.use('seaborn-darkgrid')
plt.style.use('bmh')
#plt.style.use('default')

##############################################################################
# Definição das temperaturas e pressão de entrada.

tpoints = 8
T = np.linspace(300, 1000, tpoints) #Em Kelvin
P = 1400000000000.0 #Em Pascal
    
# phases
gas = ct.Solution('gri30.cti')
#gas = ct.Solution('completo.cti')
carbon = ct.Solution('graphite.cti')

# the phases that will be included in the calculation, and their initial moles
mix_phases = [(gas, 1.0), (carbon, 0.0)]

# Espécie de combustível
fuel_species = 'C3H8'

#Laço para calcular a diferentes temperaturas de entrada no combustor
for j in range(tpoints):
    
    # Definição da variação de razão de equivalência (de 0,1 a 4,0)
    npoints = 50
    phi = np.linspace(0.1, 4.0, npoints)
##############################################################################
    
    mix = ct.Mixture(mix_phases)
    # create some arrays to hold the data
    tad = np.zeros(npoints)
    xeq = np.zeros((mix.n_species,npoints))
    graf= np.zeros(npoints)
    
    #Laço para calcular a temperatura de chama a diferentes razoes
    for i in range(npoints):
        # set the gas state
        gas.set_equivalence_ratio(phi[i], fuel_species, 'O2:1.0, N2:3.76')
    
        # create a mixture of 1 mole of gas, and 0 moles of solid carbon.
        mix = ct.Mixture(mix_phases)
        mix.T = T[j]
        mix.P = P
    
        # equilibrate the mixture adiabatically at constant P
        mix.equilibrate('HP', solver='gibbs', max_steps=1000)
    
        tad[i] = mix.T
       # print('At phi = {0:12.4g}, Tad = {1:12.4g}'.format(phi[i], tad[i]))
        xeq[:,i] = mix.species_moles
        leg= str(int(T[j]))+" K"
      
#Plotar o gráfico de Fração Molar x Razão de equivalencia para diferentes produtos 

    for i, esp in enumerate(gas.species_names):
        if esp in ['CO']:
            plt.figure(1)            
            plt.yscale('log')
            plt.semilogy(phi, xeq[i, :], label = str(int(T[j]))+" K")
            plt.xlabel('Razão de Equivalência')
            plt.ylabel('Frações Molares')
            plt.suptitle('Frações molares ' + esp + ' em função da razão de equivalência',fontsize=14)
            plt.title('Combustível Propano (C3H8)',fontsize=11)
            plt.legend()
            plt.savefig("fracao_molar_"+esp +"_"+ fuel_species + '.png')
            
        if esp in ['CO2']:
            plt.figure(2)            
            plt.yscale('log')
            plt.semilogy(phi, xeq[i, :], label = str(int(T[j]))+" K")
            plt.xlabel('Razão de Equivalência')
            plt.ylabel('Frações Molares')
            plt.suptitle('Frações molares ' + esp + ' em função da razão de equivalência',fontsize=14)
            plt.title('Combustível Propano (C3H8)',fontsize=11)
            plt.legend()
            plt.savefig("fracao_molar_"+esp +"_"+ fuel_species + '.png')
            
        if esp in ['NO']:
            plt.figure(3)            
            plt.yscale('log')
            plt.semilogy(phi, xeq[i, :], label = str(int(T[j]))+" K")
            plt.xlabel('Razão de Equivalência')
            plt.ylabel('Frações Molares')
            plt.suptitle('Frações molares ' + esp + ' em função da razão de equivalência',fontsize=14)
            plt.title('Combustível Propano (C3H8)',fontsize=11)
            plt.legend()
            plt.savefig("fracao_molar_"+esp +"_"+ fuel_species + '.png')
            
        if esp in ['NO2']:
            plt.figure(4)            
            plt.yscale('log')
            plt.semilogy(phi, xeq[i, :], label = str(int(T[j]))+" K")
            plt.xlabel('Razão de Equivalência')
            plt.ylabel('Frações Molares')
            plt.suptitle('Frações molares ' + esp + ' em função da razão de equivalência',fontsize=14)
            plt.title('Combustível Propano (C3H8)',fontsize=11)
            plt.legend()
            plt.savefig("fracao_molar_"+esp +"_"+ fuel_species + '.png')
            


    
#Plotar o gráfico de Temperatura de chama x Razão de equivalencia  
    plt.figure(5)
    plt.plot(phi, tad, label=leg)
    plt.suptitle("Temperatura de chama adiabática x Razão de equivalência",fontsize=14)
    plt.title('Combustível Propano (C3H8)',fontsize=11)
    plt.legend()
    plt.xlabel('Razão de Equivalência')
    plt.ylabel('Temperatura de Chama Adiabática [K]')
    plt.savefig('temp_chama_adiabatica' + fuel_species + '.png')
           
#Plotar os gráficos
plt.show(1)
plt.show(2)
plt.show(3)
plt.show(4)
plt.show(5)

#Plotar os gráficos de fração molar de espécies a cada temperatura de entrada no combustor
for j in range(tpoints):
    npoints = 50
    phi = np.linspace(0.1, 4.0, npoints)
##############################################################################
    
    mix = ct.Mixture(mix_phases)
    tad = np.zeros(npoints)
    xeq = np.zeros((mix.n_species,npoints))
    graf= np.zeros(npoints)
    

    for i in range(npoints):
        gas.set_equivalence_ratio(phi[i], fuel_species, 'O2:1.0, N2:3.76')
        mix = ct.Mixture(mix_phases)
        mix.T = T[j]
        mix.P = P
        mix.equilibrate('HP', solver='gibbs', max_steps=1000)
        xeq[:,i] = mix.species_moles
        leg= str(int(T[j]))+" K"
    
    for i, esp in enumerate(gas.species_names):
        if esp in ['CO', 'CO2', 'NO', 'NO2']:
            plt.figure(6)
            plt.semilogy(phi, xeq[i, :], label = esp)
            plt.yscale('log')
            plt.xlabel('Razão de Equivalência')
            plt.ylabel('Frações Molares')
            plt.suptitle('Frações molares x Razão de equivalência (T=' + leg +')',fontsize=14)
            plt.title('Combustível Propano (C3H8)',fontsize=11)
    plt.legend()
    plt.savefig('fracoes_t' + str(int(T[j])) + '_' + fuel_species + '.png')
    plt.show(6)


