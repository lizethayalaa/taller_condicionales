# Programa para indicar rl precio de venta de un articulo dado

precio_costo = float(input("Ingrese el precio de costo de articulo: "))
precio_venta = 0

if precio_costo < 3000: 
    precio_venta = precio_costo * 1.15
elif precio_costo >=  3000 and precio_costo <= 6000:
    precio_venta = precio_costo + 500
else:
    precio_venta = precio_costo * 1.25

print("El precio de venta del articulo es: $" , precio_venta) 
        