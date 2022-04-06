'''NAME
       AT-percentage

VERSION
        1.2

AUTHOR
        Hector Ulises

DESCRIPTION
        Calculate percentage of AT on a genome sequence

CATEGORY
        Genomic sequence

USAGE

    % python AT-percentage.py -i filename
    
    example
    
    % python AT-percentage.py -i sequence.txt
        
'''
#Se obtiene el nombre del archivo de la secuencia: 
file_name = input("Escribe el nombre de tu archivo y su posicion: ")

with open(file_name, 'r') as file:
        sequence = file.read()

#Se elimina el salto de linea 
sequence.rstrip("\n")

#Se obtiene la longitud de la secuencia
seq_length = len(sequence)

#Se obtienen los porcentajes
print(f"Porcentajes: ")
print(f"AT = {((sequence.count('A') + sequence.count('T')) / seq_length) * 100} %")
print(f"GC = {((sequence.count('G') + sequence.count('C')) / seq_length) * 100} %")