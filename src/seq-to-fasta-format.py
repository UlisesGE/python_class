'''
NAME
       seq-to-fasta-format.py
VERSION
        1.0
AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>
DESCRIPTION
        Este programa toma un archivo de secuencia, y lo edita de tal forma que tome 
        el formato de un archivo fasta. 
CATEGORY
        FASTA file
USAGE
         py src/seq-to-fasta.py
ARGUMENTS
    none
    
SEE ALSO   
'''

#Se agrega una excepcion en caso de que el archivo no se encuente en la ruta
try:
        # Leer las secuencias y guardarlas
        with open('../data/dna_sequences.txt','r') as file:
                sequences = file.readlines()
except IOError as io_error:
        print(f"El archivo {io_error.filename} no se enconto en la ruta especificada")
else:
        # Abrir el archivo de escritura
        FASTA = open("../results/FASTA-formated.fasta", "w")

        # Eliminar los saltos de linea y dar el formato de escritura
        for sequence in sequences:
                seq_and_id = sequence.split(' ')
                FASTA.write(f">{seq_and_id[0]}\n")
                FASTA.write(f"{seq_and_id[-1].upper().replace('-', '')}")

        # Cerrar el archivo e imprimir mensaje
        FASTA.close()
        print("Archivo Fasta generado exitosamente!")

