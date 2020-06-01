# export.py
from pip._vendor.distlib.compat import raw_input

import dbConnection
import csv, os

# Exporta baza de date in format CSV
def ExportCSV():
    querrySelect = "SELECT * FROM carte"
    try:
        db = dbConnection.CreeazaConexiune()
        c = db.cursor()
        c.execute(querrySelect)
        output = c.fetchall()
        c.close()
        db.close()
    except:
        print("Eroare la conexiunea cu baza de date!")
        raw_input("Apasati 'Enter' pentru a reveni la meniu.")
        return

    try:
        os.system('cls')
        print("===============================")
        print("Exporta baza de date in format CSV:")
        print("===============================")
        filename = raw_input("Introduceti numele fisierului (fara extensia .csv): ")
        filename = filename + ".csv"
        writer = csv.writer(open(filename, "w"))
        writer.writerow(("TITLU", "AUTOR", "EDITURA", "AN", "PRET", "GEN"))
        writer.writerows(output)
        print(filename, "Baza de date a fost exportata cu succes, apasati 'Enter' pentru a continua.")
        raw_input("")
        return
    except:
        print("Eroare la scrierea fisierului!")
        raw_input("Apasati 'Enter' pentru a reveni la meniu")