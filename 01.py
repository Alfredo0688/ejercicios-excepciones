#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

numero1 = 100
numero2 = 0

try:
    numero1/numero2
except ZeroDivisionError as e:
    print(f"El programa muestra este error '{e}' al intentar dividir el numero por 0")