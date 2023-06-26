#ejercicio del palindromo

palabra = input ('ingrese una palabra : ')
palabra = palabra.replace(' ','').lower()
newpalabra = ''
for i in palabra [::-1]:
    newpalabra += i
if palabra == newpalabra :
    print ("si es un palindromo")
if palabra != newpalabra :
    print ("no es un palindromo")

    