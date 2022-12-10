'''
NAME
	numpy.py
    
VERSION
    1.0
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	Ejercicios vistos en clase de Numpy
    
CATEGORY
	Genomic Sequence
    
USAGE

    py src/numpy.py

''' 
import numpy as np

#Ejercicio 1
#Parte 1
#Importar archivo
prod_g_mL = np.genfromtxt('./data/prod_gml.csv', delimiter=',')

#Convertir g/mL a g/L
prod_g_L = prod_g_mL * 100
print(prod_g_L)

#Parte 2
#Importar archivo 
cost = np.genfromtxt('./data/ind_cost.csv', delimiter=',')

#Convertir los costos
cost_30 = cost * 1.75
print(cost_30)
cost_35 = cost * 0.8
print(cost_35)

#Ejericio2

#Obtener costos de 1 g/L para cada cond.
cost_30_gL = cost_30 / prod_g_L[:,0]

cost_35_gL = cost_35 / prod_g_L[:,1]

#Ejericio3

#Obtener diferencias de costos
difference = cost_30_gL - cost_35_gL

#Generar vector de genes
genes_list = np.array([1, 2, 3 , 4])

#Obtener genes mas baratos
genes_30 = genes_list[difference < 0]
genes_35 = genes_list[difference > 0]
