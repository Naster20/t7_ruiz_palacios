#Ejercicio Bucles mientras 05
#Una clinica pide el peso de sus pacientes que estan entre 56-62
#Si el peso no cumple el requerimiento pedir nuevamente otro peso
peso=0
peso_invalido=(peso<=55 or peso>=63)
while   (peso_invalido):
    peso=int(input("Ingrese Peso:"))
    peso_invalido=(peso<=55 or peso>=63)
#finwhile
print("La edad es:",peso)
