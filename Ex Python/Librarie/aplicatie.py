# aplicatie.py

from pip._vendor.distlib.compat import raw_input
import os
import pip
import adaugare
import cautare
import modificare
import stergere
import export

# Meniul principal
def Menu():
    os.system('cls')
    print("""
    ================================
    1 - Adauga in baza de date
    2 - Cauta  in baza de date
    3 - Modifica inregistrare
    4 - Sterge inregistrare
    5 - Export in format CSV
    6 - Iesire
    ================================
    """)
    opt = pip._vendor.distlib.compat.raw_input("Introduceti optiunea si apasati 'Enter': ")
    return opt

# Rularea modulelor in functie de optiune
opt = ""
while opt != "6":
    opt = Menu()
    if opt == "1":
        os.system('cls')
        adaugare.MeniuAdaugaCarte()
    elif opt == "2":
        os.system('cls')
        cautare.MeniuCautaCarte()
    elif opt == "3":
        os.system('cls')
        modificare.MeniuModificaCarte()
    elif opt == "4":
        stergere.MeniuStergeCarte()
    elif opt == "5":
        export.ExportCSV()