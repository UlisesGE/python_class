'''NAME
       DNA-to-FASTA

VERSION
        1.0

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Convierte un artchivo con una secuenca a un archivo FASTA

CATEGORY
        FASTA 

USAGE
         py src/DNA-to-FASTA.py


ARGUMENTS
    none

    
SEE ALSO
        


'''
#Abrir el archivo y copiar el contenido a una lista; abrir un archivo tipo FASTA
sequence_file = open("dna.txt", "r")
sequence = sequence_file.readlines()
sequence_file.close()
FASTA = open("sequence.fasta", "w")

# Se solicita un ID
ID = input("Introduzca un ID de la secuencia: ")

#Se meten los contenidos al archivo ya creado
FASTA.write(f">{ID}\n{sequence}")

#Se cierra el archivo
sequence_file.close()
