'''
NAME
	EntrezSearch.py
    
VERSION
    1.0
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	- Genera un termino a buscar automaticamente, y regresa los IDs de bases de datos donde encontro informacion
    
CATEGORY
    Database
    
USAGE
    py src/EntrezSearch.py 
    
ARGUMENTS
    -s --sequence

    
SEE ALSO
        
''' 

import argparse
import re
from Bio import Entrez
from pprint import pprint

#Se agrega el paso de argumentos 
arg_parser = argparse.ArgumentParser(description = "Genera un termino, y regresa IDs de bases de datos con match")

arg_parser.add_argument("-t", "--termino",
                    type=str,
                    help="Organismo y genes en el formato: 'Organism1: Gene1, Gene2; Organism2: ...",
                    required=True)

                    
arg_parser.add_argument("-o", "--output",
                    help="archivo de output",
                    metavar="path/to/file",
                    required=True)

args = arg_parser.parse_args()

Entrez.email = "hectorg@lcg.unam.mx"

def term(termino):
    #Se inicializa una lista para guardar los terminos
    term_list = []
    #Se da un formato adecuado para cada organismo, delimitados por ;
    for termino in termino.split(";"):
        
        #Se separan los genes para cada organismo
        input = term.split(":")
        term = input[0] + "[Orgn] AND ("

        #Se les da un fromato adecuado
        i = True
        for gen in input[1].replace(" ", "").split(","):
            if i:
                term += gen + '[Gene]'
            else:
                term += " OR " + gen + '[Gene]'
            i = False
        term += ")"

        #Se guardan en la lista
        term_list += [term]
    #Se regresa la lista
    return(term_list)        

def search(term):
    with open(out, "w") as outfile:
        for term in term:
            DB_IDs = []
            organisms = term.split("[Orgn]")
            organism = organisms[0]
            outfile.write(f"*{organism}\n")

            handle = Entrez.egquery(term = term)
            record = Entrez.read(handle)

            for row in record["eGQueryResult"]:
                if row["Count"] != 0 and row["Count"] != "Error":
                    DB_IDs += [row["DbName"]]
            for DB in DB_IDs:
                IDs = []

                db_record = Entrez.read(Entrez.esearch(db = DB, term = term)

                IDs = db_record["IdList"]
                DB = DB.split(",")
                DB_ID = DB[0] + ": "
                DB_IDs = DB_ID + str(IDs).replace('[', '').replace(']', '').replace("'", "")

                outfile.write(f"{DB_IDs}\n")
    return()
    
    



termino = args.termino
out = args.output

terminos = term(termino)
DataBases = search(terminos, out)