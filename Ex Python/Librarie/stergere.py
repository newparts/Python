# stergere.py

import pymysql, os, dbConnection

# Executa o interogare SQL pentru stergerea din baza de date
from pip._vendor.distlib.compat import raw_input


def StergeCarte(carteStergere):
    try:
        queryDelete = 'DELETE FROM carte WHERE titlu = %s' % carteStergere
        db = dbConnection.CreeazaConexiune()
        c = db.cursor()
        c.execute(queryDelete)
        db.commit()
        c.close()
        db.close()
        raw_input("Inregistrarea a fost stearsa cu success! Apasati 'Enter' pentru a continua.")
    except:
        print("Eroare la stergerea inregistrarii")
        raw_input("Apasati 'Enter' pentru a continua.")

# Afisare meniu stergere
def MeniuStergeCarte():
    os.system('cls')
    print("===============================")
    print("Sterge inregistrarea")
    print("===============================")
    campCautare="titlu"
    carteStergere = raw_input("\nIntroduceti titlul cartii pe care doriti sa o stergeti:\t")
    carteStergere = "\"%s\"" % (carteStergere)
    querySelect = "SELECT * FROM carte WHERE %s = %s" % (campCautare,carteStergere)
    try:
        db = dbConnection.CreeazaConexiune()
        c = db.cursor()
        c.execute(querySelect)
        searchResult = c.fetchall()
        # if searchResult[0] == ():
        #  raise
    except:
        print("Eroare la accesarea inregistrarii in baza de date!")
        raw_input("Apasati 'Enter' pentru a continua.")
        return

    print("===============================")
    print("Informatii despre cartea care va fi stearsa")
    print("===============================")
    print("Titlu:\t", searchResult[0][0])
    print("Autor:\t", searchResult[0][1])
    print("Editura:\t", searchResult[0][2])
    print("An:\t", searchResult[0][3])
    print("Pret:\t", searchResult[0][4])
    print("Gen:\t:", searchResult[0][5])
    print("===============================")
    print("""     
    Sunteti sigur ca doriti sa stergeti cartea? \n     
    Introduceti optiunea si apasati 'Enter' (D/d = da, Orice altceva = Nu)     
    """)
    opt = raw_input("\t")
    if (opt == "D" or opt == "d"):
        StergeCarte(carteStergere)
    else:
        c.close()
        db.close()
        raw_input("Inregistrarea NU a fost stearsa! Apasati 'Enter' pentru a continua.")