#!/usr/bin/python3
import subprocess


USUARIOS = ["juan", "cristina", "maria", "nicolas", "fernando"]



def main():
    crear_directorio(USUARIOS)


def crear_directorio(directorios):
    for directorio in directorios:
        resultado = subprocess.run(["mkdir", directorio], text=True, capture_output=True)
        if resultado.returncode == 0:
            print(f"Se ha creado con exito el directorio {directorio}")
        else:
            print(f"No se ha creado el directorio {directorio}, esto es real hermano, yo no me junto con tigres que no saben tener respeto por los mayores.")








if __name__ == "__main__":
    main()