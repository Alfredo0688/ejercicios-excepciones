#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sinembargo, también intenta crear el archivo si no existe.

try:
    #intento leer el archivo de texto
    with open("archivoPerdido.txt","r") as  archivo_lectura:
        print(archivo_lectura.read())

except FileNotFoundError as e:
    print(f"No se encontró el archivo : {e}")