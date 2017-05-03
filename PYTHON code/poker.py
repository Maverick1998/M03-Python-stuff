#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


salir = False 
saldo = 100
apuesta_m = 10
salir_ap = False
aleatori = randint(1,13)
jugador = aleatori
maquina = aleatori

while salir == False:
	
	j1 = input("Introduzca su apuesta: ")
	if saldo < 10:
		print "Minimo 10"
	else:
		if saldo >=10:
			
			saldo = saldo - j1
	 		print "Tu monedero dispone de:", saldo , "$"


	if aleatori == 1:
		jugador = "A"
	
	if aleatori == 11:
		jugador = "J"
	
	if aleatori == 12:
		jugador = "Q"
	
	if aleatori == 13:
		jugador = "K"
	
	print "El jugador va con un: ", jugador , "La maquina va con: " , maquina

	if jugador > maquina:
		print "Gana jugador"
	else:
		if jugador < maquina:
			print"Gana la maquina"


		
	if saldo < 10:
		salir = True
	

