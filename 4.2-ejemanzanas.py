cantidad= int (input ("ingrese la cantidad de manzanas que deseea "))
precio = int (input("ingrese el precio "))
nombre = input ("ingresa tu nombre")
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
    
    
    
    
    
    