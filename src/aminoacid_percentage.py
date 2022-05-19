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

#Se pide al usuaro que introduzca la secuencia de aminoacidos asi como el aminoaciod del que quiere el porcentaje
sequence = input('Introduce una secuencia de aminoácidos:')

aminoacid = input('Introduce el aminoácido para obtemer el porcentaje:')

#Se define la variable con un nombre cool pq las ranas son cool
def rana(sequence, aminoacid):
    #Se obtiene la longitud de la secuencia introducida por el usuario
    sequence_length = len(sequence)
    #Se calcula el porcentaje del aminoacido y se regresa el valor obtenido
    return (sequence.upper().count(aminoacid.upper())/sequence_length)*100

#se hacen asserts para probar la funcion
assert rana("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert rana("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert rana("msrslllrfllfllllpplp", "L") == 50
assert rana("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

#Se garda lo que regresa la funcion en la variable percentage
percentage = rana(sequence, aminoacid)
#Se imprime el valor obtenido
print(f"El total de {str(aminoacid.upper())} de la secuenca es {percentage}%")
