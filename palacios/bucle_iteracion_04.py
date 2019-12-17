#Ejercicio iteracion 04
#Estado civil
import os
sociedad=os.sys.argv[1]
estado_civil=os.sys.argv[2]
for estado_civil in sociedad:
    if  (estado_civil=="s"):
        print("Soltera")
    if  (estado_civil=="c"):
        print("Casada")
    if  (estado_civil=="v"):
        print("Viuda")
    if  (estado_civil=="d"):
        print("Divorciada")
    #finif
#finfor
