# Pido que ingrese las coordenandas cartesianas (x,y) del punto
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

#Verififco en que cuadrante se encuentra el punto
if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante.")        
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuarto cuadrante.")    
elif x == 0 and y == 0:
    print("El punto se encuentra sobre el origen.")
elif x == 0 and y != 0:
    print("El punto se encuentra sobre ele eje y.") 
else:
    print("El punto se encuentra sobre el eje x.")
    