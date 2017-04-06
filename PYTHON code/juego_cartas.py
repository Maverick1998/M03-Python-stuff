#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
aleatori = randint(1,13)
aleatori1 = randint(1,13)
jugador1 = randint
jugador2 = randint
cartas=randint 
aleatorio2=randint(1,4)

if aleatorio2 == 1:
	 cartas="Pica"
if aleatorio2 == 2:
	cartas ="Diamante"
if aleatorio2 == 3:
	cartas ="Trebol"
if aleatorio2 == 4:
	cartas ="Corazones"
	

if aleatori1 == 1:
	jugador1 ="1"
	
if aleatori1 == 2:
	jugador1 ="2"


if aleatori1 == 3:
	jugador1 ="3"
	
	
if aleatori1 == 4:
	jugador1 ="	4"


if aleatori1 == 5:
	jugador1 ="5"


if aleatori1 == 6:
	jugador1 ="6"


if aleatori1 == 7:
	jugador1 ="7"
	

if aleatori1 == 8:
	jugador1 ="8"
	

if aleatori1 == 9:
	jugador1 ="9"

if aleatori1 == 10:
	jugador1 ="10"

if aleatori1 == 11:
	jugador1 ="J"
	
if aleatori1 == 12:
	jugador1 ="Q"

if aleatori1 == 13:
	jugador1 ="K"
	
print "Maquina 1 saca",jugador1,cartas

if aleatori == 1:
	jugador2 ="1"

if aleatori == 2:
	jugador2 ="2"


if aleatori == 3:
	jugador2 ="3"
	
	
if aleatori == 4:
	jugador2 ="4"


if aleatori == 5:
	jugador2 ="5"


if aleatori == 6:
	jugador2 ="6"


if aleatori == 7:
	jugador2 ="7"
	

if aleatori == 8:
	jugador2 ="8"
	

if aleatori == 9:
	jugador2 ="9"

if aleatori == 10:
	jugador2 ="10"

if aleatori == 11:
	jugador2 ="J"
	
if aleatori == 12:
	jugador2 ="Q"

if aleatori == 13:
	jugador2 ="K"
	
print "Maquina 2 saca",jugador2,cartas


if jugador1==jugador2 :
	print "empate",
		
if (jugador1 > jugador2 ):
	print "Gana la maquina 1"
	
else:
	
	print "Gana la maquina 2"
