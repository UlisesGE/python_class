'''NAME
       AT-percentage

VERSION
        1.7

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
import argparse

arg_parser = argparse.ArgumentParser(description = "Calcula el contenido AT y GC, dado una ruta de un archivo de secuencia de DNA")

arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)

arg_parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    required=False)
                    
arg_parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)

args = arg_parser.parse_args()
file_name = args.input

#Se agrega un try-except para detectar errores en la ruta y/o nombre del archivo
try:
        with open(file_name, 'r') as file:
                file_content = file.read()
except IOError as io_error:
        print(f"El archivo {io_error.filename} no se encontró en la ruta especificada")

else:
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
