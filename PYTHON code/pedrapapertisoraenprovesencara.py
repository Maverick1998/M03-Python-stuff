#coding:utf-8
 
piedra=1
papel=2
tijeras=3
jugador1=raw_input("¿Que desea el amo?: 1piedra 2papel 3tijera")
jugador2=raw_input("Que desea hacer mi otro amo? 1piedra 2papel 3tijera")
if jugador1 == jugador2:
    print "empate"
if (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 == 3 and jugador2 == 2):
    print "Gana jugador 2	"
else:	
    print "jugador1 gana"
       
    






