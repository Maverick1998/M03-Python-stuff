#coding: utf-8
from subprocess import call
import math
print("Suma:           1") 
print("Resta:          2") 
print("Multiplicación: 3") 
print("División:       4") 
#print("Potencia:       5") 
#print("Raíz cuadrada:  6") 
print("Salir           7")
opcion = int(input("Escriba el número de lo que desee hacer: "))

while not(opcion == 7):
    if not(opcion > 0 and opcion < 8):
        call('clear')
        print"Esa opcion no existe"

    if opcion == 1:
        numero = int(input("Primer numero: "))
        numero2 = int(input("Segundo numero: "))
        print ('El resultado es ', numero + numero2)

    if opcion == 2:
        numero = int(input("Primer numero: "))
        numero2 = int(input("Segundo numero: "))
        print ('El resultado es ', numero - numero2)

    if opcion == 3:
        numero = int(input("Primer numero: "))
        numero2 = int(input("Segundo numero: "))
        print ('El resultado es ', numero * numero2)

    if opcion == 4:
        numero = int(input("Primer numero: "))
        numero2 = int(input("Segundo numero: "))
        print ('El resultado es ', numero / numero2)

    print("suma:           1") 
    print("resta:          2") 
    print("multiplicación: 3") 
    print("división:       4") 
    print("potencia:       5") 
    print("raiz cuadrada:  6") 
    print("salir           7")
    opcion = int(input("Escriba un número positivo: "))
