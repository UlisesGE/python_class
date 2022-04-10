'''NAME
       sequence-trim.py

VERSION
        1.0

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este programa recortará la porción del adaptador de una secuencia dada, y lo pondrá en un archivo nuevo llamado trimmed.txt

CATEGORY
        dna sequence

USAGE
         py src/DNA-to-FASTA.py


ARGUMENTS
         none

    
SEE ALSO
        


'''

with open('4_input_adapters.txt','r') as file:
        adapters = file.readlines()

#print(adapters)
trimmed = open('trimmed.txt', "w")

for adapter in adapters:
        trimmed_seq = adapter[14:]
        trimmed.write(trimmed_seq)
