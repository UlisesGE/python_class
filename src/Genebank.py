'''
NAME
	Genebank.py
    
VERSION
    1.0
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	Obtiene las secuencias en las que todos los nucleotidos superan el umbral, 
    imprime el numero de seuencias, y guarda los ids y secuencias en un archivo.
    
CATEGORY
    DNA sequence
    
USAGE
    py src/SecuenciasYFormatos2.py -path/to/file
    
ARGUMENTS
    -i --input
    -g --gene

    
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

                    
arg_parser.add_argument("-g", "--gene",
                    help="Nombre del gen a buscar",
                    type=str,
                    required=True)

args = arg_parser.parse_args()

file_name = args.input

#Se agrega un try-except para detectar errores en la ruta y/o nombre del archivo
try:
        with open(file_name, 'r') as file:
                file_content = file.read()
except IOError as io_error:
        print(f"El archivo {io_error.filename} no se encontró en la ruta especificada")

else:
        for gb_record in SeqIO.parse(file_name, "genbank"):
            for feature in gb_record.features:
                if feature.type == args.gene:
                    print(f"GeneBank gene {args.gene} information: \n")
                    print(f"Sequence: {gb_record.seq[feature.location.nofuzzy_start:feature.location.nofuzzy_end]}")
                    DNA = gb_record.seq[feature.location.nofuzzy_start:feature.location.nofuzzy_end]
                    RNA = DNA.transcribe()
                    print(f"Transcript: {RNA}")
                    protein = DNA.translate()
                    print(f"Protein: {protein}")
