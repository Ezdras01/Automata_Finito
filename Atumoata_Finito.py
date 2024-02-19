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
        print("El automata tendra", estados, "estados")
        
    except ValueError:
        print("Por favor ingresa un número")
      
        continue
    
    if estados <= 0:
        print("Por favor ingresa un número valido para los estados")
        continue
    else:
        break

alfabeto = str(input("Ingresa el alfabeto que tendra tu automata, sepralos por comas (Σ): "))
print("El automata tendra el siguiente alfabeto:", alfabeto)

while True:
    try:
        inicio = int(input("Ingresa el estado inicial de tu automata (q0): "))        
    except ValueError:
        print("Por favor ingresa un número")
        continue
    if inicio <= 0 or inicio > estados:
        print("Por favor ingresa un número valido para el estado inicial")
        continue
    
    else:
        print("El estado inicial de tu automata es: q",inicio)
        break
   
   