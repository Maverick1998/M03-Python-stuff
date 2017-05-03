#coding: utf8

print "Hola, bienvenidos al piedra papel tijera"
print "1-Piedra"
print "2-Papel"
print "3-Tijera"

tecla = input("Seleciona la primera opcion: ")
tecla1 = input("Seleciona la segunda opcion: ")
contador = 0
exit = False

while exit == False:
	
	contador = contador + 1 	

	
	if tecla == 1 and tecla1 == 1:
		
		print "Empate" 
	
	if tecla == 1 and tecla1 == 2:
		
		print "Gana el papel"
	
	if tecla == 1 and tecla1 == 3:
		
		print "Gana la piedra"

	if tecla == 2 and tecla1 == 1:
		
		print "Gana el papel" 
	
	if tecla == 2 and tecla1 == 2:
		
		print "Empate"

	if tecla == 2 and tecla1 == 3:
		
		print "Gana la tijera"
		
	if tecla == 3 and tecla1 == 1:
		
		print "Gana la piedra" 
	
	if tecla == 3 and tecla1 == 2:
	
		print "Gana la tijera"
	
	if tecla == 3 and tecla1 == 3:
		
		print "Empate"

		

if contador == 2:
		exit = True
		
	
	
	
	
	
