#Ejercicio Bucles mientras 01
#En un examen de programacion la nota debe estar entre 0 y 20
#Si la nota ingresada no es validad, pedir nota nuevamente
nota=-1
nota_invalida=(nota<0 or nota>20)
while   (nota_invalida):
    nota=int(input("Ingrese Nota:"))
    nota_invalida=(nota<0 or nota>20)
#finwhile
print("Nota Valida",nota)
