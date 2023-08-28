#Investigando el modulo sys
import sys

#sys.version para revisar la version que se emplea
print(f"Versión del módulo sys: {sys.version}")

#sys.modules para revelar los modules importados de python
print(sys.modules)

#sys.stdin para ingresar directamente a la linea de comando como si de un input se tratara.
for i in sys.stdin: 
    if 'salir' == i.rstrip(): 
        break
    print(f'Input : {i}') 
  
print("Programa finalizado!")

#sys.stdout para definir la salida del interpretador
sys.stdout.write("Esta razon de salida es personalizado!")

#sys.exit([codigo]) para finalizar el programa con un mensaje de salida opcional
sys.exit('cerrando mediante este codigo personalizado.........................')