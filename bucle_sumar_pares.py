#!/usr/bin/env python
# -*- coding: utf-8 -*-

total = 0
for numero in range (1,9):
	print numero
	if numero %2 == 0:
		total = total + numero
		numero = numero + 1
	if numero == 5:
		salir = True
print "La suma de los pares es:",total
	
