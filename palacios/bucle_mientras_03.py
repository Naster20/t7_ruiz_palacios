#Ejercicio Bucles mientras 03
#Una farmacia da descuento del 20% a personas que se llaman carlos
#si la persona tiene otro nombre, pedir nuevamente otro nombre.
nombre=""
nombre_invalido=(nombre!="carlos")
while   (nombre_invalido):
    print("nombre invalido")
    nombre=input("Ingrese nombre:")
    nombre_invalido=(nombre!="carlos")
#finwhile
print("Nombre valido")
print("Descuento del 20%")
