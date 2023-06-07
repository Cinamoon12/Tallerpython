cantidad= int (input ("ingrese la cantidad de manzanas que deseea "))
precio = int (input("ingrese el precio "))
if cantidad > 10 :
    descuento = (cantidad * precio) * .10
    print (f"tienes un descuento de {descuento}") 
    print (f"vas a pagar esto {(cantidad * precio) - descuento}") 