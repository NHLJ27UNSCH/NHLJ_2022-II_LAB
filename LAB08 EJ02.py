#Investigando el modulo sys
import sys


#sys.version para reviar la version
print(f"Versión del módulo sys: {sys.version}")

#sys.stdin para ingresar directamente a la linea de comando como si de un input se tratara.
for i in sys.stdin: 
    if 'salir' == i.rstrip(): 
        break
    print(f'Input : {i}') 
  
print("Programa finalizado!")

#sys.stdout para mostrar la salida del interpretador
sys.stdout.write("No es directamente un print!")