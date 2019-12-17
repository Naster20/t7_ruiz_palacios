# EJERCICIO N° 03
producto=""
precio=90
precio_invalido=(precio>80)
while(precio_invalido):
    producto=input("Ingrese Producto :")
    precio=float(input("Ingrese Precio :"))
    precio_invalido=(precio>80)
#fin_while
print("Producto :",producto,",Su Precio es valido :",precio,"soles")
