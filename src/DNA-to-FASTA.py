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
         python DNA-to-FASTA.py


ARGUMENTS
    none

    
SEE ALSO
        


'''
#Abrir el archivo y copiar el contenido a una lista; abrir un archivo tipo FASTA

#Se agrega una excepcion en caso de que el archivo no se encuente en la ruta que deberia, especificada por el ejercicio
try:
        sequence_file = open("data/dna.txt", "r")

        sequence = sequence_file.readlines()
        sequence_file.close()
except IOError as io_error:
        print(f"El archivo {sequence_file} no se encuentra.\n")

else:
        FASTA = open("results/sequence.fasta", "w")

        # Se solicita un ID
        ID = input("Introduzca un ID de la secuencia:\n")

        #Se meten los contenidos al archivo ya creado
        FASTA.write(f">{ID}\n{sequence}")

        #Se cierran los archivos
        sequence_file.close()
        FASTA.close()
