# modificare.py
from pip._vendor.distlib.compat import raw_input

import dbConnection


def MeniuModificaDVD():
    print("===============================")
    print("Modificare inregistrare in baza de date:")
    print("===============================")

    titluDVD = raw_input("\n Introduceti titlul filmului pe care doriti sa-l modificati: ")

    querrySelectTitlu = "SELECT * FROM dvd WHERE titlu = \"%s\"" % titluDVD

    try:
        db = dbConnection.CreeazaConexiune()
        c = db.cursor()
        c.execute(querrySelectTitlu)
        rezultat = c.fetchall()
        # if rezultat[0] == ():
        #   raise
    except:
        print("Eroare la accesarea inregistrarii in baza de date!")
        raw_input("Apasati 'Enter' pentru a continua.")
        return

    try:
        print("===============================")
        print("Filmul care va fi modificat:")
        print("===============================")
        print("1 - Titlu:\t", rezultat[0][0])
        print("2 - Actor principal:\t", rezultat[0][1])
        print("3 - Actor secundar:\t", rezultat[0][2])
        print("4 - An:\t", rezultat[0][3])
        print("5 - Gen:\t", rezultat[0][4])
        print("===============================")

        opt = raw_input("Introduceti numele campului pe care doriti sa-l modificati, si apasati 'Enter': ")

        titluModificat = False
        campModificat = ""
        nouaValoare = ""
        if opt == "1":
            campModificat = "titlu"
            nouaValoareTitlu = raw_input("Introduceti noul titlu: ")
            nouaValoare = "\"%s\"" % nouaValoareTitlu
            titluModificat = True
        elif opt == "2":
            campModificat = "actor_principal"
            nouaValoare = raw_input("Introduceti noul nume pentru actorul principal: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "3":
            campModificat = "actor_secundar"
            nouaValoare = raw_input("Introduceti noul nume pentru actorul secundar: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "4":
            campModificat = "an"
            nouaValoare = raw_input("Introduceti anul: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "5":
            campModificat = "gen"
            print("===============================")
            print("Alegeti genul pe care doriti sa-l modificati:")
            print("1 - Drama")
            print("2 - Horror")
            print("3 - Comedy")
            print("4 - Romance")

            optiune = raw_input("Introduceti noua valoare pentru genul filmului: ")

            if optiune == "1":
                nouaValoare = "\"Drama\""
            elif optiune == "2":
                nouaValoare = "\"Horror\""
            elif optiune == "3":
                nouaValoare = "\"Comedie\""
            elif optiune == "4":
                nouaValoare = "\"Romantic\""

        querryUpdate = "UPDATE dvd SET %s = %s WHERE titlu = \"%s\"" % (campModificat, nouaValoare, titluDVD)

        db = dbConnection.CreeazaConexiune()
        c = db.cursor()
        c.execute(querryUpdate)
        db.commit()

        if titluModificat:
            querrySelect = "SELECT * FROM dvd WHERE titlu = \"%s\"" % nouaValoareTitlu
            c = db.cursor()
            c.execute(querrySelect)
            rezultatModificare = c.fetchall()
            c.close()
            db.close()
    except:
        print("Eroare la modificare inregistrarii!")
        raw_input("Apasati 'Enter' pentru a continua.")
        return

    print("===============================")
    print("Intregistrare modificata:")
    print("===============================")
    print("1 - Titlu:\t", rezultatModificare[0][0])
    print("2 - Actor principal:\t", rezultatModificare[0][1])
    print("3 - Actor secundar:\t", rezultatModificare[0][2])
    print("4 - An:\t", rezultatModificare[0][3])
    print("5 - Gen\t", rezultatModificare[0][4])
    print("===============================")
    raw_input("Apasati 'Enter' pentru a continua")