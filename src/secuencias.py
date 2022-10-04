'''
NAME
	secuencias.py
    
VERSION
    1.0
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	Obwtiene la cadena proteica de cualquiera de los ORFS, y elige la cadena de mayor longitud
    
CATEGORY
    DNA sequence
    
USAGE
    py src/secuencias.py
    
ARGUMENTS
    none
    
SEE ALSO
        
''' 

import argparse
from turtle import position
from Bio.Seq import Seq, MutableSeq
from Bio import SeqUtils
from itertools import chain

arg_parser = argparse.ArgumentParser(description = "Obtiene el peptido mas grande de una secuencia proteica dada")

#Se asignan argumentos para que el programa use
arg_parser.add_argument("-s", "--sequence",
                    #metavar="path/to/file",
                    help="sequence",
                    required=True)


#arg_parser.add_argument("-s", "--size",
#                    help="Size of the region",
#                    type=int,
#                    required=False)
arguments = arg_parser.parse_args()

sequence = Seq(arguments.sequence)
def LongestPeptide(sequence):
    ORFs = SeqUtils.nt_search(str(sequence), 'ATG')
    Complementary_ORFs = SeqUtils.nt_search(str(sequence.complement), 'ATG')
    complement = (sequence.complement)

    if len(ORFs) != 1 & len(Complementary_ORFs) != 1:
        Peptides = (sequence[position:].translate(to_stop = True) for position in ORFs[1:])

        ComplementaryPeptides = (complement[position:].translate(to_stop = True) for position in Complementary_ORFs[1:])

        AllPeptides = chain(Peptides, ComplementaryPeptides)

        return(max(AllPeptides))


    else: 
        return("No se encontro un ORF en la secuencia: " + sequence)

    print(len(ORFs))
    print(len(Complementary_ORFs))

Peptide = LongestPeptide(sequence)

print(f"El peptido mas grande codificado es {Peptide}")