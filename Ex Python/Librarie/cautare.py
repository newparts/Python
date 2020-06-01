# cautare.py

import pymysql, os
from pip._vendor.distlib.compat import raw_input

import dbConnection

# Executa o interogare pentru cautare in baza de date
def CautaCarte(campCautare, textCautare):
    querrySelect = "SELECT * FROM carte WHERE %s = %s" % (campCautare, textCautare)
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
    print("Cautare Carte in baza de date:")
    print("===============================")
    if output == ():
        print("Nu a fost gasita nicio inregistrare!")
        print("===============================")
    for entry in output:
        print("Titlu:\t", entry[0])
        print("Autor:\t", entry[1])
        print("Editura:\t", entry[2])
        print("An:\t", entry[3])
        print("Pret:\t", entry[4])
        print("Gen:\t", entry[5])
        print("===============================")
    raw_input("\n\nApasati 'Enter' pentru a continua: ")

# Afiseaza meniul pentru a cauta in baza de date
def MeniuCautaCarte():
    print("""         
        ===============================         
        Alegeti criteriul de cautare:         
        1 - Dupa titlu         
        2 - Dupa autor        
        3 - Dupa editura        
        4 - Dupa an   
        5 - Dupa pret       
        6 - Dupa gen""")
    opt = raw_input("\nIntroduceti optiunea si apasati 'Enter': ")
    campCautare = ""
    textCautare = ""

    if opt == "1":
        campCautare = "titlu"
        textCautare = raw_input("Introduceti titlul cartii: ")
        textCautare = "\"%s\"" % (textCautare)
    elif opt == "2":
        campCautare = "autor"
        textCautare = raw_input("Introduceti numele autorului: ")
        textCautare = "\"%s\"" % (textCautare)
    elif opt == "3":
        campCautare = "editura"
        textCautare = raw_input("Introduceti numele editurii: ")
        textCautare = "\"%s\"" % (textCautare)
    elif opt == "4":
        campCautare = "an"
        textCautare = int(raw_input("Introduceti anul: "))
    elif opt == "5":
        campCautare = "pret"
        textCautare = int(raw_input("Introduceti pretul: "))
    elif opt == "6":
        campCautare = "gen"
        print("""         
        Introduceti genul:         
        1 - Beletristica         
        2 - Stiinta        
        3 - Comedie         
        4 - Romantic
        5 - SF
        6 - Enciclopedie      
        """)
        optiuneGen = raw_input("\t")
        if optiuneGen == "1":
            textCautare = "\"Beletristica\""
        elif optiuneGen == "2":
            textCautare = "\"Stiinta\""
        elif optiuneGen == "3":
            textCautare = "\"Comedie\""
        elif optiuneGen == "4":
            optiuneGen = "\"Romantic\""
        elif optiuneGen == "5":
            optiuneGen = "\"SF\""
        elif optiuneGen == "6":
            optiuneGen = "\"Enciclopedie\""
    else:
        print("Ati introdus date gresite!")
        raw_input("Apasati 'Enter' pentru a reveni la meniu.")
        return
    CautaCarte(campCautare, textCautare)