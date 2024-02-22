#!/usr/bin/python3
import subprocess
import sys

def main():
    limpiar_pantalla()
    conocer_ordenadores_encendidos()

def limpiar_pantalla():
    subprocess.run("clear")

def conocer_ordenadores_encendidos():
    ip = sys.argv[1]
    resultado = subprocess.run(["ping","-c","1","-W", "1", ip], text=True, capture_output=True)
    if resultado.returncode == 0:
        print(f"El ordenador {ip} esta encendido.")
    else:
        print(f"El ordenador {ip} no esta encendido.")




if __name__ == "__main__":
    main()