#!/usr/bin/python3
import sys
import subprocess

def main():
    limpiar_pantalla()
    if son_argumentos_correctos():
        mostrar_info()
    else: 
        print("El numero de argumentos es incorrecto")
        sys.exit()

def mostrar_info():
    nombre = sys.argv[1]
    apellido = sys.argv[2]
    edad = sys.argv[3]
    modulo = sys.argv[4]

    print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y el modulo que mas me gusta es {modulo}.")


def limpiar_pantalla():
    subprocess.run("clear")


def son_argumentos_correctos():
    argumentos = sys.argv[1:]
    if len(argumentos) != 4:
        return False
    else:
        edad = argumentos[2]
        if not edad.isnumeric():
            return False
        else:
            return True







if __name__ == "__main__":
    main()