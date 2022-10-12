'''
NAME
	SecuenciasYFormatos2.py
    
VERSION
    1.
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	Obtiene las secuencias en las que todos los nucleotidos superan el umbral, 
    imprime el numero de seuencias, y guarda los ids y secuencias en un archivo.
    
CATEGORY
    DNA sequence
    
USAGE
    py src/SecuenciasYFormatos2.py -
    
ARGUMENTS
    -s --sequence

    
SEE ALSO
        
''' 
import argparse
from Bio import SeqIO

#Se agrega el paso de argumentos 
arg_parser = argparse.ArgumentParser(description = "Obtiene las secuencias en las que todos los nucleotidos superan el umbral, imprime el numero de seuencias, y guarda los ids y secuencias en un archivo.")

arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with fastq sequences",
                    required=True)

arg_parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    required=False)
                    
arg_parser.add_argument("-u", "--umbral",
                    help="Valor del umbral a usar",
                    type=int,
                    required=True)

args = arg_parser.parse_args()

file_name = args.input

def Quality_Check(file_name):
    with open(args.output, 'w') as file:
        i = 0
        for seq in SeqIO.parse(args.input, 'fastq'):

            if(all(x > int(args.umbral) for x in seq.letter_annotations['phred_quality'])):
                file.write(f'{seq.id}\n{str(seq.seq)}\n')
                i += 1
    return(f"El archivo {args.output} ha sido creado")


#Se agrega un try-except para detectar errores en la ruta y/o nombre del archivo
try:
        with open(file_name, 'r') as file:
                file_content = file.read()
except IOError as io_error:
        print(f"El archivo {io_error.filename} no se encontró en la ruta especificada")

else:
        Test = Quality_Check(args.input)
