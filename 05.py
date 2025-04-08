#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. 
# Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

valor1 = "pepe"
valor2 = 0

try:
    resultado = valor1 / valor2
except ZeroDivisionError as e:
    print(f"El número no puede dividirse por 0 : {e}")

except TypeError as e:
    print(f"Los valores que intervienen en la división deben ser númericos : {e}")

else:

    print(f"Los valores ingresados fueron {valor1} y {valor2} dando como resultado {resultado}")

finally:
    print("Fin del programa")