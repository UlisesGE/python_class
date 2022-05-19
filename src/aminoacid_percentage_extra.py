'''NAME
       aminoacid_percentage

VERSION
        1.0

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene el porcentaje de un aminoácido dado de una secuencia dada por el usuario.

CATEGORY
        Script

USAGE
         python aminoacid_percentage_extra.py


ARGUMENTS
       None

    
SEE ALSO
        Ninguno

'''
sequence = input('Introduce una secuencia de aminoacidos: ')
aminoacids = input('Introduce aminoacidos a buscar: ')
def sapo(sequence, aminoacids = ['A','I','L','M','F','W','Y','V']):
    sequence_length = len(sequence)
    count = 0
    for i in range(0, len(aminoacids)):
        count += str(sequence[i]).upper().count(str(aminoacids[i]))

    return(count/sequence_length)*100
percentage = sapo(sequence, aminoacids)

print(percentage)