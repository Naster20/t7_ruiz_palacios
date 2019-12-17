#Ejercicio bucles mientras 04
#En una clinica se atiende ancianos apartir de 60 a 110 anios de edad
#Si la edad es ingresada es inferior a 60, pedir de nuevo.
edad=0
edad_invalida=(edad<60 or edad>110)
while   (edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<60 or edad>110)
#finwhile
print("Edad:",edad)
