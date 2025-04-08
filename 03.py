#Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
# Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario.

diccionario = {"Nombre":"Alfredo","Apellido":"Nuñez","Edad": 37}

try:
    print(diccionario["Nombre"])
    print(diccionario["esProgramador"])
except KeyError as e:
    print(f"Clave no encontrada, error mostrado '{e}'")