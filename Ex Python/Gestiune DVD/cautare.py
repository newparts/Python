# cautare.py

import pymysql, os
from pip._vendor.distlib.compat import raw_input

import dbConnection

# Executa o interogare pentru cautare in baza de date
def CautaDVD(campCautare, textCautare):
    querrySelect = "SELECT * FROM dvd WHERE %s = %s" % (campCautare, textCautare)
    try:
        db=dbConnection.CreeazaConexiune()
        c=db.cursor()
        try:
            c.execute(querrySelect)
        except Exception as e:
            print(e)
        output = c.fetchall()
        c.close()
        db.close()
    except:
        print("Eroare la conexiunea cu baza de date!  ", e)
        raw_input("Apasati tasta 'Enter' pentru a continua.")
        return

    os.system('cls')
    print("===============================")
    print("Cautare DVD in baza de date:")
    print("===============================")
    if output == ():
        print("Nu a fost gasita nicio inregistrare!")
        print("===============================")
    for entry in output:
        print("Titlu:\t", entry[0])
        print("Actor principal:\t", entry[1])
        print("Actor secundar:\t", entry[2])
        print("An:\t", entry[3])
        print("Gen:\t", entry[4])
        print("===============================")
    raw_input("\n\nApasati 'Enter' pentru a continua: ")

# Afiseaza meniul pentru a cauta in baza de date
def MeniuCautaDVD():
    print("""         
        ===============================         
        Alegeti criteriul de cautare:         
        1 - Dupa titlu         
        2 - Dupa actorul principal         
        3 - Dupa actorul secundar         
        4 - Dupa an         
        5 - Dupa gen""")
    opt = raw_input("\nIntroduceti optiunea si apasati 'Enter': ")
    campCautare = ""
    textCautare = ""

    if opt == "1":
        campCautare = "titlu"
        textCautare = raw_input("Introduceti titlul filmului: ")
        textCautare = "\"%s\"" % (textCautare)
    elif opt == "2":
        campCautare = "actor_principal"
        textCautare = raw_input("Introduceti numele actorului principal: ")
        textCautare = "\"%s\"" % (textCautare)
    elif opt == "3":
        campCautare = "actor_secundar"
        textCautare = raw_input("Introduceti numele actorului secundar: ")
        textCautare = "\"%s\"" % (textCautare)
    elif opt == "4":
        campCautare = "an"
        textCautare = int(raw_input("Introduceti anul: "))
    elif opt == "5":
        campCautare = "gen"
        print("""         
        Introduceti genul:         
        1 - Drama         
        2 - Horror         
        3 - Comedie         
        4 - Romantic         
        """)
        optiuneGen = raw_input("\t")
        if optiuneGen == "1":
            textCautare = "\"Drama\""
        elif optiuneGen == "2":
            textCautare = "\"Horror\""
        elif optiuneGen == "3":
            textCautare = "\"Comedie\""
        elif optiuneGen == "4":
            optiuneGen = "\"Romantic\""
    else:
        print("Ati introdus date gresite!")
        raw_input("Apasati 'Enter' pentru a reveni la meniu.")
        return
    CautaDVD(campCautare, textCautare)