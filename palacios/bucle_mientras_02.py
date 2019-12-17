#Ejercicio Bucles mientras 02
#Pedir un numero multiplo de 7, si el numero
#No cumple el requisito volver a pedir numero.
n=1
numero_invalido=((n%7)!=0)
while   (numero_invalido):
    n=int(input("Ingrese n:"))
    numero_invalido=((n%7)!=0)
#finwhile
print("N=",n)
