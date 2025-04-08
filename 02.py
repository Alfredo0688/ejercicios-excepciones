#Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

cadena = "El ballet cósmico ha comenzado"
numero = 888

try:
    numero + cadena
except TypeError as e:
    print(f"El programa muestra este error '{e}' al intentar sumar los valores")