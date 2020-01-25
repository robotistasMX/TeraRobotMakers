def calculadora():
    n1 = float(input("Dame el primer número: "))
    n2 = float(input("Dame el segundo número: "))
    print("Suma:" + str(n1 + n2))
    print("Resta: " + str(n1 - n2))
    print("Multiplicación: " + str(n1 * n2))
    if(n2 != 0):
        print("División: " + str(n1 / n2))
    else:
        print("Jaja, no se puede dividir entre 0 :'v")    
while (True):
    calculadora()
    continuar = input("Desea hacer otra operación?: ")
    if(continuar == "si"):
        print("Ta' gueno, pues ") 
        continue
    else:
        break
print("Hasta laaa próximaaaaaaaa... ")    