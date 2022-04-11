'''NAME
       seq-to-fasta-format.py

VERSION
        1.0

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este programa toma un archivo de secuencia, y lo edita de tal forma que tome el formato de un archivo fasta. 

CATEGORY
        FASTA file

USAGE

         py src/seq-to-fasta.py


ARGUMENTS
    none

    
SEE ALSO
        


'''

with open('dna_sequences.txt','r') as file:
        sequences = file.readlines()
        sequences = sequences.split("\n")

FASTA = open("FASTA-fromated.fasta", "w")

for sequence in sequences:
        seq_and_id = line.split(' ')
        FASTA.write(f">{seq_and_id[0]}\n")
        FASTA.write(f"{seq_and_id[-1].upper().replace('-', '')}\n")

