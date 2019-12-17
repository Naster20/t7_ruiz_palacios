# EJERCICIO N° 04
producto=""
pedido=10
pedido_invalido=(pedido<11 or pedido>20)
while(pedido_invalido):
    producto=input("Ingrese Producto :")
    pedido=int(input("Ingrese Pedido :"))
    pedido_invalido=(pedido<11 or pedido>20)
#fin_while
print("Producto :",producto,",Su pedido es valido :",pedido,"unidades")
