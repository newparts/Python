# modificare.py
from pip._vendor.distlib.compat import raw_input

import dbConnection


def MeniuModificaCarte():
    print("===============================")
    print("Modificare inregistrare in baza de date:")
    print("===============================")

    titluCarte = raw_input("\n Introduceti titlul cartii pe care doriti sa o modificati: ")

    querrySelectTitlu = "SELECT * FROM carte WHERE titlu = \"%s\"" % titluCarte


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
        print("Cartea care va fi modificata:")
        print("===============================")
        print("1 - Titlu:\t", rezultat[0][0])
        print("2 - Autor:\t", rezultat[0][1])
        print("3 - Editura:\t", rezultat[0][2])
        print("4 - An:\t", rezultat[0][3])
        print("5 - Pret:\t", rezultat[0][4])
        print("6 - Gen:\t", rezultat[0][5])
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
            campModificat = "autor"
            nouaValoare = raw_input("Introduceti noul autor: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "3":
            campModificat = "editura"
            nouaValoare = raw_input("Introduceti editura noua: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "4":
            campModificat = "an"
            nouaValoare = raw_input("Introduceti anul nou: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "5":
            campModificat = "pret"
            nouaValoare = raw_input("Introduceti pretul nou: ")
            nouaValoare = "\"%s\"" % nouaValoare
        elif opt == "6":
            campModificat = "gen"
            print("===============================")
            print("Alegeti genul pe care doriti sa-l modificati:")
            print("1 - Beletristica")
            print("2 - Stiinta")
            print("3 - Comedie")
            print("4 - Romantic")
            print("5 - SF")
            print("6 - Enciclopedie")

            optiune = raw_input("Introduceti noua valoare pentru genul cartii: ")

            if optiune == "1":
                nouaValoare = "\"Beletristica\""
            elif optiune == "2":
                nouaValoare = "\"Stiinta\""
            elif optiune == "3":
                nouaValoare = "\"Comedie\""
            elif optiune == "4":
                nouaValoare = "\"Romantic\""
            elif optiune == "5":
                nouaValoare = "\"SF\""
            elif optiune == "6":
                nouaValoare = "\"Enciclopedie\""

        querryUpdate = "UPDATE carte SET %s = %s WHERE titlu = \"%s\"" % (campModificat, nouaValoare, titluCarte)

        db = dbConnection.CreeazaConexiune()
        c = db.cursor()
        c.execute(querryUpdate)
        db.commit()

        if titluModificat:
            querrySelect = "SELECT * FROM carte WHERE titlu = \"%s\"" % nouaValoareTitlu
            c = db.cursor()
            c.execute(querrySelect)
            rezultatModificare = c.fetchall()
            c.close()
            db.close()
    except:
        print("Eroare la modificarea inregistrarii!")
        raw_input("Apasati 'Enter' pentru a continua.")
        return

    print("===============================")
    print("Intregistrare modificata cu succes:")
    print("===============================")
    print("1 - Titlu:\t", rezultatModificare[0][0])
    print("2 - Autor:\t", rezultatModificare[0][1])
    print("3 - Editura:\t", rezultatModificare[0][2])
    print("4 - An:\t", rezultatModificare[0][3])
    print("5 - Pret:\t", rezultatModificare[0][4])
    print("6 - Gen\t", rezultatModificare[0][5])
    print("===============================")
    raw_input("Apasati 'Enter' pentru a continua")