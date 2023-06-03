# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:17:40 2023

@author: Pedro
"""
# Saudação e explicar o que fazer ao utilizador
saudacao = ("Olá, digita de seguida 5 números, um de cada vez. Obrigado!")
print(saudacao)

num1 = int(input("Digita o primeiro número: "))
num2 = int(input("Digita o segundo número: "))
num3 = int(input("Digita o terceiro número: "))
num4 = int(input("Digita o quarto número: "))
num5 = int(input("Digita o quinto número: "))

# Agregar os números numa lista
numeros=[num1, num2, num3, num4, num5]

# for para fazer o loop e verificar quais os números pares
for numero in numeros:
    if numero % 2==0:
        print(numero)
print("Estes são os números pares.")