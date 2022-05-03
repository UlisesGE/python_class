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
        file_content = file.read()

#Se elimina el salto de linea 
file_content.rstrip("\n")

#Se obtiene la longitud de la secuencia
longitud = len(file_content)

AT_content = ((file_content.count('A') + file_content.count('T')) / longitud) * 100
GC_content = ((file_content.count('G') + file_content.count('C')) / longitud) * 100 

#Se obtienen los porcentajes
print(f"Porcentajes: ")
print(f"AT = {AT_content} %")
print(f"GC = {GC_content} %")
