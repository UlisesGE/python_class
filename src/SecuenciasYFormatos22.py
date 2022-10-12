'''
NAME
	SecuenciasYFormatos22.py
    
VERSION
    1.0
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	Obtiene informacion de las anotaciones de un archivo GeneBank
    
    
CATEGORY
    Genomic File Format
    
USAGE
    py src/SecuenciasYFormatos22.py -
    
ARGUMENTS
    -s --sequence

    
SEE ALSO
        
''' 
import argparse
from Bio import SeqIO

#Se agrega el paso de argumentos 
arg_parser = argparse.ArgumentParser(description = "Obtiene informacion de las anotaciones de un archivo GeneBank.")

arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with fastq sequences",
                    required=True)
                  
#arg_parser.add_argument("-u", "--umbral",
#                    help="Valor del umbral a usar",
#                    type=int,
#                    required=True)

args = arg_parser.parse_args()

for gb_record in SeqIO.parse(args.input, "genebank"):
    print("\n Annotations: \n")
    print('ID', gb_record.annotations['organism'])
    print('Date', gb_record.annotations['date'])
    print("\n Features: \n")
    print('Country', gb_record.features[0].qualifiers['country'])
    print('Molecular type', gb_record.features[0].qualifiers['mol_type'])



