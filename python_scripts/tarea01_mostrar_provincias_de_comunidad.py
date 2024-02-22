#!/usr/bin/python3
import subprocess, sys

COMUNIDADES = ["andalucia", "canarias", "cantabria", "cataluña", "galicia", "islas-baleares", "la-rioja", "navarra", "pais-vasco", "aragon", "castilla-la-mancha", "castilla-y-león", "comunidad-valenciana", "extremadura", "madrid", "murcia", "asturias"]

def main():
    argumentos = sys.argv[1:]
    limpiar_pantalla()
    
    print(es_argumento_correcto(argumentos))


def limpiar_pantalla():
    subprocess.run("clear")

def es_argumento_correcto(argumentos):    
    if len(argumentos) != 1:
        return False
    
    comunidad = argumentos[0]
    if comunidad not in COMUNIDADES:
        return False
    
    return True


if __name__ == '__main__':
    main()