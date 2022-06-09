'''NAME
       aminoacid_percentage

VERSION
        1.5

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene el porcentaje de un aminoácido dado de una secuencia dada por el usuario.

CATEGORY
        Script

USAGE
         python aminoacid_percentage.py -s AILMFWYV -a M


ARGUMENTS
        -a --aminoacids 
        -s --sequence
        -h --help

    
SEE ALSO
        Ninguno

'''
#Se importa argparse
import argparse

#Se llama a la funcion rana del modulo de porcentaje de aminoacidos
from AminoacidTools import rana

arg_parser = argparse.ArgumentParser(description = "Calcula el porcentaje de un aminoaciod, dado una secuencia de un polipeptido")

#Se asignan argumentos para que el programa use
arg_parser.add_argument("-s", "--sequence",
                    metavar="S E Q U E N C E",
                    help="Sequence from which to calcula the percentage",
                    type = str,
                    required=False)

arg_parser.add_argument("-a", "--aminoacid",
                    help="aminoacid you want the percentage of",
                    type = str,
                    required=True)

arg_parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)
arguments = arg_parser.parse_args()


#Se garda lo que regresa la funcion en la variable percentage
percentage = rana(sequence = arguments.sequence, aminoacid = arguments.aminoacid, decimals = arguments.round)
#Se imprime el valor obtenido
print(f"El porcentaje del aminoacido {str(arguments.aminoacid)} es: {percentage}")
