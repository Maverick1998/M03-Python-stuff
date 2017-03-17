# coding: utf­8
### bucle-test.py
### Robert Rebaza
### Plantilla de bucle ejemplo


print "1. Entrar"
print "2. Salir"

num1 = input("Introduce un numero :")
salir = "N"

while salir == "N":
    if  num1 == 2 :                                                      # Salir del programa 
        salir = "S"

    else:
        if num1 == 1 :                                                   # Entro al bucle
            ### introduzco lo pedido
            print "bienvenido"
            print "1. Entrar"
            print "2. Salir"
            num1 = input("Introduce un numero :")
            salir = "N"

        else:
            if not num1 == 1 :
                print "esa opcion no existe"
