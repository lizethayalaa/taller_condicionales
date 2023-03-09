 # Programa que solicicta los ingresos mensuales y si tiene deuda actualmente
ingresos = float(input("Ingrese sus ingresos mensuales: "))
deuda = input("¿Tiene alguna deuda actualmente? (Si/No): ")

# Verificacion de elegibiidad 
if ingresos >= 945200 and deuda.lower() == "no":
    print("Felicidades, usted es elegible para un prestamo bancario.")
    # Solicitud del monto del prestamo 
    monto = float(input("¿Cuanto dinero desea solicitar en prestamo? "))
    print("Su prestamo de $" , monto, " ha sido aprobdo. ")
else:
    print("Lo siento, usted no cumple con los requisitos para obtener un prestamo bancario.") 