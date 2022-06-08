'''NAME
       aminoacid_percentage

VERSION
        1.3

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene el porcentaje de un aminoácido dado de una secuencia dada por el usuario.

CATEGORY
        Script

USAGE
         python aminoacid_percentage.py


ARGUMENTS
       None

    
SEE ALSO
        Ninguno

'''

import argparse

arg_parser = argparse.ArgumentParser(description = "Calcula el porcentaje de un aminoaciod, dado una secuencia de un polipeptido")

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

#Se pide al usuaro que introduzca la secuencia de aminoacidos asi como el aminoaciod del que quiere el porcentaje
#sequence = input('Introduce una secuencia de aminoácidos:')

#aminoacid = input('Introduce el aminoácido para obtener el porcentaje:')

arguments = arg_parser.parse_args()

#Se define la variable con un nombre cool pq las ranas son cool
def rana(sequence, aminoacid):
    '''
    Returns the percentage of aminoacids in a sequence
        Parameters: 
                sequence (str): User's aminoacid sequence
                aminoacid (str): The speceific aminoacid the user wants to get the percentage of
        Returns:
                percentage(float): The percentage of a speceific aminoacid in the given sequence
    '''
    sequence_length = len(sequence)
    #Se calcula el porcentaje del aminoacido y se regresa el valor obtenido
    return (sequence.upper().count(aminoacid.upper())/sequence_length)*100

#se hacen asserts para probar la funcion
assert rana("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert rana("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert rana("msrslllrfllfllllpplp", "L") == 50
assert rana("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


percentage = rana(sequence = arguments.sequence, aminoacid = arguments.aminoacid)
print(f"El porcentaje del aminoacido {str(arguments.aminoacid)} es: {percentage}")
#Se garda lo que regresa la funcion en la variable percentage
#percentage = rana(sequence, aminoacid)
#Se imprime el valor obtenido
#print(f"El total de {str(aminoacid.upper())} de la secuenca es {percentage}%")
