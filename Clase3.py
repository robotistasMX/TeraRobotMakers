zapatos  = ["formales" , "deportivos" , "jordan" , "chanclas", "nike","Reebook"] 
"""
seleccion = int(input("Seleccione unos cacles: "))
if(seleccion > (len(zapatos) - 1)  or seleccion < 0):
    print("Híjole, qué se me hace\nque no se va a poder")
else:
    print("Tu selección fue: " + zapatos[seleccion])
"""
for i in range(len(zapatos)):
    print(zapatos[i])