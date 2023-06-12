year = int (input("ingrese el anio "))
if year % 4 != 0 : #nos referimos a que no es divisible entre 4 
    print ("no es bisiesto")
elif year % 4 == 0 and year  % 100 != 0: 
    print ("es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0 :
    print ("no es bisisesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print ("es bisiesto")