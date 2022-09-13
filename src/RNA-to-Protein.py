'''NAME
       RNA-to-Protein

VERSION
        1.0

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene el peptido codificado por una secuencia de DNA o RNA dada por el usuario

CATEGORY
        Script

USAGE
         python RNA-to-Protein.py -s DNA/RNAsequece


ARGUMENTS
        - s --sequence
    
SEE ALSO
        Ninguno

'''

import argparse
import re

arg_parser = argparse.ArgumentParser(description = "Obtiene las regiones ricas en AT y su posición, dado un archivo de secuencia y el tamaño minimo de la region")

#Se asignan argumentos para que el programa use
arg_parser.add_argument("-s", "--sequence",
                    help="User's sequence",
                    type=str,
                    required=True)

arguments = arg_parser.parse_args()

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

seq = arguments.sequence

def test_rna(rna):
    no_rna = re.findall(r"[^ATGCU]", rna)
    try:
        if re.search(r"[^ATGCU]", rna):
            raise ValueError
    except ValueError:
        print(f"La secuencia genética contiene caracteres no identificados como nucleótidos: {no_rna}")
        print("Desea intentar de nuevo?(y/n)")
        result=input()
        if result == "y":
            newrna=input("Introduzca su nueva secuencia de RNA:")
            newrna = newrna.upper()
            test_rna(newrna)
        else:
            exit()
    else:
        return(rna)