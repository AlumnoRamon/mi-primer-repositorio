#!/usr/bin/python3
import subprocess
import sys


def main():
    limpiar_pantalla()

    argumentos = sys.argv[1:]
    if not son_argumentos_correctos(argumentos):
        print("El mes introducido no existe. Introduzcalo en minúsculas.")
        sys.exit

        mes = argumentos[0]
        mes = str(convertir_mes(mes))
        año = argumentos[1]
        imprimir_calendario(convertir_mes(mes), año)
        
    #     año = sys.argv[2]
    # else:
    #     print("El mes introdcido no existe. Introduzcalo en minusculas.")
    #     sys.exit()
    # imprimir_calendario
    # print(convertir_mes("enero"))
    # print(convertir_mes("febrero"))
    # print(convertir_mes("marzo"))
    # print(convertir_mes("abril"))
    # print(convertir_mes("mayo"))
    # print(convertir_mes("junio"))
    # print(convertir_mes("julio"))
    # print(convertir_mes("agosto"))
    # print(convertir_mes("septiembre"))
    # print(convertir_mes("octubre"))
    # print(convertir_mes("noviembre"))
    # print(convertir_mes("diciembre"))
    # print(convertir_mes("error"))


def imprimir_calendario():
    # if sys.argv[1] == "enero":
    #     subprocess.run(["cal", "1", "2001"])
    # elif sys.argv[1] == "febrero":
    #     subprocess.run(["cal", "2", "2001"])
    # elif sys.argv[1] == "marzo":
    #     subprocess.run(["cal", "3", "2001"])
    # elif sys.argv[1] == "abril":
    #     subprocess.run(["cal", "4", "2001"])
    # elif sys.argv[1] == "mayo":
    #     subprocess.run(["cal", "5", "2001"])
    ...




def son_argumentos_correctos(argumentos):
    if len(argumentos) == 2:
        return False
    
    mes_letra = sys.argv[1]
    mes = convertir_mes(mes_letra)
    if mes == None:
        return False
    

    año = sys.argv[2]
    if año.isnumeric():
        return True
    else:
        return False        





    
def convertir_mes(mes):
    match mes:
        case "enero":
            return 1
        case "febrero":
            return 2
        case "marzo":
            return 3
        case "abril":
            return 4
        case "mayo":
            return 5
        case "junio":
            return 6
        case "julio":
            return 7
        case "agosto":
            return 8
        case "septiembre":
            return 9
        case "octubre":
            return 10
        case "noviembre":
            return 11
        case "diciembre":
            return 12
        case _:
            return None


def limpiar_pantalla():
    subprocess.run("clear")












if __name__ == "__main__":
    main()