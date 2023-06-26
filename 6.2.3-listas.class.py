#ejercicio del pangrama
# frase para el ejercicio: "benjamin pidio una bebida de kiwi y fresa, noe sin verguenza la mas exquisita champana del menu"

abecedario = "abcdefghijklmnsopqrstuvwxyz" 
frase = input ("ingrese la frase a comprobar ")

faltan = False
for i in abecedario :
    if not i in frase :
        faltan = True 
        
if faltan == False :
    print ("es pangram")
else :
    print ("no es pangram")
    