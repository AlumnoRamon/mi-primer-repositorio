#!/usr/bin/python3
import subprocess,sys



def main():
    argumentos = sys.argv[1:]
    print(argumentos)
    limpiar_pantalla()
    if not son_argumentos_correctos(argumentos):
        print("Los argumentos no son correctos")
        sys.exit()
    else:
        numero_de_copias = int(argumentos[0])
        fichero = argumentos[1]
        nuevo_nombre = argumentos[2]
        copiar_ficheros(numero_de_copias, fichero, nuevo_nombre)

def limpiar_pantalla():
    subprocess.run("clear")


def son_argumentos_correctos(argumentos):

    if len(argumentos)!=3:
        return False
    
    numero_de_copias = argumentos[0]
    if not numero_de_copias.isnumeric():
        return False 
    
    fichero = sys.argv[1]
    if fichero == None:
        return False
    
    nuevo_nombre = sys.argv[2]
    if nuevo_nombre == None:
        return False
       
    return True


def copiar_ficheros(numero_de_copias, fichero, nuevo_nombre):
    for i in range(1, numero_de_copias+1):
        if i < 10:
            subprocess.run(["cp", fichero, f"{nuevo_nombre}0{i}"])
        else:
            subprocess.run(["cp", fichero, f"{nuevo_nombre}{i}"])
    













if __name__ == '__main__':
    main()