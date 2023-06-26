# ejercicio del contador 
contador = 1 

numero = int (input ("ingrese el numero : "))
while numero > 20 or numero <0 :
    numero = int (input ("ingrese el numero : "))
contador += 1 

print ("numero ingresado", numero)
print ("numero de intentos", contador)