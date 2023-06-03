# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:13:37 2023

@author: Pedro
"""
# Definir uma função, neste caso o cálculo do retângulo

def calcula_area_retangulo(comprimento, altura):
    return str(comprimento * altura )+"cm2"

# Pedimos ao utilizador que insira os dados para o cálculo

comprimento = float(input("Qual a medida do comprimento do retângulo: "))
altura = float(input("Qual a altura do retângulo: "))

print(calcula_area_retangulo(comprimento, altura))