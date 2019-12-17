# EJERCICIO N° 02
alumno=""
nota=-1
nota_invalida=(nota<0 or nota>20)
while(nota_invalida):
    alumno=input("Ingrese Alumno :")
    nota=float(input("Ingrese nota :"))
    nota_invalida=(nota<0 or nota>20)
#fin_while
print("Alumno :",alumno,",Su nota es valida :",nota,"de nota")
