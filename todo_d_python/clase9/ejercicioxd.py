"""
Desafío Genérico 1
Realizar una función llamada par_o_impar:

Recibirá un número por parámetro
Imprimirá Par si el número es par
Imprimirá Impar si el número es impar
Si se ingresa algo que no sea número debe indicar que se ingrese un número. (Para los más audaces)
"""

def par_o_impar(numero):
    """Determina si un número es par o impar"""
    if numero % 2 == 0:
        mensaje = "Es un número par"
    else:
        mensaje = "Es un número impar"
    return mensaje

def funcion_principal():
    
    while True:
        entrada = input("Ingrese un número entero (0 sale): ")
        if entrada == "0":
            break
        if entrada.isdigit():
            numero = int(entrada)
        else:
            continue
        mensaje_recibido = par_o_impar(numero)
        print(mensaje_recibido)

funcion_principal()
