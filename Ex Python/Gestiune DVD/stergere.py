# stergere.py

import pymysql, os, dbConnection

# Executa o interogare SQL pentru stergerea din baza de date
from pip._vendor.distlib.compat import raw_input


def StergeDVD(dvdStergere):
    try:
        queryDelete = 'DELETE FROM dvd WHERE titlu = %s' % dvdStergere
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
def MeniuStergeDVD():
    os.system('cls')
    print("===============================")
    print("Sterge inregistrare")
    print("===============================")
    campCautare="titlu"
    dvdStergere = raw_input("\nIntroduceti titlul DVD-ului pe care doriti sa-l stergeti:\t")
    dvdStergere = "\"%s\"" % (dvdStergere)
    querySelect = "SELECT * FROM dvd WHERE %s = %s" % (campCautare,dvdStergere)
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
    print("Informatii despre DVD care va fi sters")
    print("===============================")
    print("Titlu:\t", searchResult[0][0])
    print("Actor principal:\t", searchResult[0][1])
    print("Actor secundar:\t", searchResult[0][2])
    print("An:\t", searchResult[0][3])
    print("Gen:\t:", searchResult[0][4])
    print("===============================")
    print("""     
    Sunteti sigur ca doriti sa stergeti DVD-ul? \n     
    Introduceti optiunea si apasati 'Enter' (D/d = da, Orice altceva = Nu)     
    """)
    opt = raw_input("\t")
    if (opt == "D" or opt == "d"):
        StergeDVD(dvdStergere)
    else:
        c.close()
        db.close()
        raw_input("Inregistrarea NU a fost stearsa! Apasati 'Enter' pentru a continua.")