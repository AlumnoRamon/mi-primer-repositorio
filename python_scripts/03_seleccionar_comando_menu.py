#!/usr/bin/python3

import subprocess
import sys

def main():
    limpiar_pantalla()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion == 1:
            mostrar_fecha()
        elif opcion == 2:
            mostrar_quien_soy()
        elif opcion == 3:
            mostrar_quien_esta_conectado()
        elif opcion == 4:
            mostrar_calendario()
        elif opcion == 5:
            mostrar_contraseña()
        elif opcion == 6:
            cerrar_aplicacion()

def pedir_opcion() -> int:
    while True:
        respuesta = input("Introduzca una opción del menú: ")
        
        if respuesta.isnumeric():
            opcion = int(respuesta)
            print(f"El numero introducido es {opcion}")

            if opcion <1 or opcion >6:
                print("Debe introducir una opción permitida.")
            else:
                return opcion
        else:
            print("Debe introducir un número.")

def mostrar_fecha():
    subprocess.run(["date", '+"%d/%m/%Y"'])

def mostrar_quien_soy():
    subprocess.run("whoami")

def mostrar_quien_esta_conectado():
    subprocess.run(["who"])

def mostrar_calendario():
    subprocess.run(["cal"])

def cerrar_aplicacion():
    sys.exit()

def limpiar_pantalla():
    subprocess.run("clear")

def mostrar_contraseña():
    print("EN OBRAS")

def mostrar_menu():
    print("\n---------- Menú ----------")
    print("\t1) Mostrar fecha.")
    print("\t2) Mostrar quién soy.")
    print("\t3) Mostrar quién esta conectado.")
    print("\t4) Mostrar el calendario.")
    print("\t5) Mostrar la contraseña (EN MANTENIMIENTO).")
    print("\t6) Cerrar el script.")
 
    
if __name__ == "__main__":
    main()