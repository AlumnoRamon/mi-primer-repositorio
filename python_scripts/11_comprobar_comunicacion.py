#!/usr/bin/python3
import subprocess
import sys


def main():
    limpiar_pantalla()
    comprobar_ping()


def comprobar_ping():
    ip = sys.argv[1]
    resultado = subprocess.run(["ping","-c","1",ip], text=True, capture_output=True)
    if resultado.returncode == 0:
        print("Existe resultado con el equipo 8.8.8.8")
    else:
        print("No existe comunicacion.")

        
def limpiar_pantalla():
    subprocess.run("clear")


if __name__ == "__main__":
    main()