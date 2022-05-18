'''NAME
       aminoacid_percentage

VERSION
        1.1

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene el porcentaje de un aminoácido dado de una secuencia dada por el usuario.

CATEGORY
        Script

USAGE
         python aminoacid_percentage.py


ARGUMENTS
       

    
SEE ALSO
        Ninguno

'''


sequence = input('Introduce una secuencia de aminoácidos:')

aminoacid = input('Introduce el aminoácido para obtemer el porcentaje:')


def rana(sequence, aminoacid):
    sequence_length = len(sequence)
    return (sequence.upper().count(aminoacid.upper())/sequence_length)*100

assert rana("AILMFWYV", "Y") == 12.5

percentage = rana(sequence, aminoacid)
print(f"El total de {str(aminoacid.upper())} de la secuenca es {percentage} %")

