#Cortez Espejel Ezra Lehi  
#Fecha de creacion: 19/02/2024
#Automata finito

menu="""
Bienvendio al automata finito ingresa los datos que se te pedirán a continuacion:
"""
print(menu)
while True:
    try:
        estados = int(input("Ingresa los estados que tendra tu automata (Q): "))
    except ValueError:
        print("Por favor ingresa un número")
      
        continue
    
    if estados <= 0:
        print("Por favor ingresa un número valido para los estados")
        continue
    else:
        break