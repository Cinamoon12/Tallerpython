import os
from time import sleep
secs = 3
nombre = input ("ingresa tu nombre ")
precio = int (input("ingrese el precio "))
cantidad= int (input ("ingrese la cantidad de manzanas que deseea :(si pones un 0 me salgo) "))
while cantidad != 0 :
    if cantidad == 18 :     
        descuento = (cantidad * precio) * .20
        print (f"tienes un descuento de {descuento}") 
        print (f"vas a pagar esto {(cantidad * precio) - descuento}") 
    elif nombre == "viniza" :
        descuento = (cantidad * precio) * .20
        print ("se aplica descuento del 20% ")
        print (f"tienes un descuento de {descuento}") 
    elif cantidad > 10 :
        descuento = (cantidad * precio) * .10 
        print ("se aplica descuento del 10% ")
        print (f"tienes un descuento de {descuento}") 
        print (f"vas a pagar esto {(cantidad * precio) - descuento}") 
    cantidad= int (input ("ingrese la cantidad de manzanas que deseea :(si pones un 0 me salgo) "))
    
    sleep (secs)
    os.system ("cls")
    