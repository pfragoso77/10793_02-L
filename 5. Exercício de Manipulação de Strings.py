# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:17:37 2023

@author: Pedro
"""

nome_completo = input("Escreva o seu nome completo: ")

nome = nome_completo.split()
numero_de_elementos_numa_lista = len(nome)
for i in nome:
    print(nome[::-1])

print("Obrigado, pela sua participação")




