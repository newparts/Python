# adaugare.py
from pip._vendor.distlib.compat import raw_input

import dbConnection

# Executa o interogare SQL pentru a adauga in baza de date
def AdaugaDVD(titlu, actorPrincipal, actorSecundar, an, gen):
    sqlInsert = 'INSERT INTO dvd values ("%s", "%s", "%s", "%s", "%s")' %  (titlu, actorPrincipal, actorSecundar, an, gen)
    try:
        db=dbConnection.CreeazaConexiune()
        c=db.cursor()
        try:
            c.execute(sqlInsert)
        except Exception as e:
            print("Eroare: ", e)
        db.commit()
        c.close()
        db.close()
        raw_input("Inregistrarea a fost adaugata cu success - apasati 'Enter' pentru a continua: ")
    except:
        print("Eroare la adaugarea in baza de date")
        raw_input("Apasati 'Enter' pentru a continua.")

# Afiseaza meniul pentru adaugarea in baza de date
def MeniuAdaugaDVD():
    print("===============================")
    print("Adaugare DVD in baza de date:")
    print("===============================")
    titlu = raw_input("Introduceti titlul filmului: ")
    actorPrincipal = raw_input("Introduceti numele actorului din rolul principal: ")
    actorSecundar = raw_input("Introduceti numele actorului din rolul secundar: ")
    an = raw_input("Introduceti anul aparitiei: ")
    gen = raw_input("Introduceti genul filmului:\n - 1 - Drama, 2 - Horror, 3 - Comedie, 4 - Romantic: ")
    if gen == "1":
        gen = "Drama"
    elif gen == "2":
        gen = "Horror"
    elif gen == "3":
        gen = "Comedie"
    elif gen == "4":
        gen = "Romantic"
    else:
        print("Ati introdus informatii gresite!")
        raw_input("Apasati 'Enter' pentru a va intoarce la meniu.")
        return

    AdaugaDVD(titlu, actorPrincipal, actorSecundar, an, gen)