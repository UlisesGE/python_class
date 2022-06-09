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

#Se importan expresiones regulares
import re

#Se crea una excepcion nueva
class NotAnAminoacidError(Exception):
        pass

#Se define una funcion nueva
def rana(sequence, aminoacid, decimals = 4):
    '''
    Returns the percentage of aminoacids in a sequence
        Parameters: 
                sequence (str): User's aminoacid sequence
                aminoacid (str): The speceific aminoacid the user wants to get the percentage of
        Returns:
                percentage(float): The percentage of a speceific aminoacid in the given sequence
    '''

    import re
    #Se revisa si el usuario introdujo una secuencia
    if not sequence:
        #Si no, se solicita la ruta del archivo que contenga una
        file_name = input("Introduzca la ruta y el nombre el archivo de secuencia: \n")
        try:
            with open(file_name, 'r') as f:
                sequence = str(f.read())
                if re.search("[^GALMFWKQESPVICYHRNDT]", sequence):
                    #Si no, se avisa al usuario que la secuencia no es valida
                    raise NotAnAminoacidError(f"La secuencia no es valida")
                else:
                    sequence_length = len(sequence)
                    #Se calcula el porcentaje del aminoacido y se regresa el valor obtenido
                    percent = (sequence.upper().count(aminoacid.upper())/sequence_length)*100
                    percent = round(percent, decimals)
                    return percent
        except IOError as io_error:
            print(f"El archivo no se encontró. \n")
            
    else:
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