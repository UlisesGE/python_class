'''NAME
       aminoacid_percentage

VERSION
        1.4

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
#Se importa re
import re

arg_parser = argparse.ArgumentParser(description = "Calcula el porcentaje de un aminoaciod, dado una secuencia de un polipeptido")

#Se asignan argumentos para que el programa use
arg_parser.add_argument("-s", "--sequence",
                    metavar="S E Q U E N C E",
                    help="Sequence from which to calcula the percentage",
                    type = str,
                    required=True)

arg_parser.add_argument("-a", "--aminoacid",
                    help="aminoacid you want the percentage of",
                    type = str,
                    required=True)

arg_parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)

arguments = arg_parser.parse_args()

class NotAnAminoacidError(Exception):
        pass

#Se define la variable con un nombre cool pq las ranas son cool
def rana(sequence, aminoacid, decimals = 4):
    '''
    Returns the percentage of aminoacids in a sequence
        Parameters: 
                sequence (str): User's aminoacid sequence
                aminoacid (str): The speceific aminoacid the user wants to get the percentage of
        Returns:
                percentage(float): The percentage of a speceific aminoacid in the given sequence
    '''
    #Se revisa que la secuencia solo contenga aminoacidos validos
    if re.search("[^GALMFWKQESPVICYHRNDT]", sequence):
            #Si no, se avisa al usuario que la secuencia no es valida
            raise NotAnAminoacidError(f"La secuencia no es valida")
    else:
        sequence_length = len(sequence)
        #Se calcula el porcentaje del aminoacido y se regresa el valor obtenido
        percent = (sequence.upper().count(aminoacid.upper())/sequence_length)*100
        percent = round(percent, decimals)
        return percent

#Se garda lo que regresa la funcion en la variable percentage
percentage = rana(sequence = arguments.sequence, aminoacid = arguments.aminoacid, decimals = arguments.round)
#Se imprime el valor obtenido
print(f"El porcentaje del aminoacido {str(arguments.aminoacid)} es: {percentage}")
