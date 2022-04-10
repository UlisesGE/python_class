'''NAME
       sequence-trim.py

VERSION
        1.1

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

#se abre el archivo de las secuencias, y se guerdan en una lista
with open('4_input_adapters.txt','r') as file:
        adapters = file.readlines()

#Se crea un archivo nuevo, donde se guardarán las secuencias recortadas
trimmed = open('trimmed.txt', "w")

#se hace un ciclo for que recortará cada secuencia, y las guardará en un archivo final
for adapter in adapters:
        trimmed_seq = adapter[14:]
        trimmed.write(trimmed_seq)
