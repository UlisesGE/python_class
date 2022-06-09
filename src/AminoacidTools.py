'''NAME
       AminoacidTools

VERSION
        1.0

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Herramienta para el manejo de secuencias de polipeptidos

CATEGORY
        Protein sequence

USAGE
         import AminoacidTools

    
SEE ALSO
        Ninguno

'''

import re

class NotAnAminoacidError(Exception):
        pass

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
    import re
    if re.search("[^GALMFWKQESPVICYHRNDT]", sequence):
            #Si no, se avisa al usuario que la secuencia no es valida
            raise NotAnAminoacidError(f"La secuencia no es valida")
    else:
        sequence_length = len(sequence)
        #Se calcula el porcentaje del aminoacido y se regresa el valor obtenido
        percent = (sequence.upper().count(aminoacid.upper())/sequence_length)*100
        percent = round(percent, decimals)
        return percent