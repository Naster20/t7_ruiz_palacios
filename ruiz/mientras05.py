# EJERCICIO N° 05
producto=""
cantidad=5
cant_inval=(cantidad<6 or cantidad>10)
while(cant_inval):
     producto=input("Ingrese Producto :")
     cantidad=int(input("Ingrese la cantidad :"))
     cant_inval=(cantidad<6 or cantidad>10)
#fin_while
print("Producto :",producto,cantidad,"Unidades su cantidad es valida")
