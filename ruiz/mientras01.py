# EJERCICIO N° 01
usuario=""
edad=10
edad_invalida=(edad<18 or edad>80)
while(edad_invalida):
    usuario=input("Ingrese Usuario :")
    edad=int(input("Ingrese edad :"))
    edad_invalida=(edad<18 or edad>80)
#fin_while
print("Usuario :",usuario,",Su edad es valida :",edad,"años")
