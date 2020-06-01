# adaugare.py
from pip._vendor.distlib.compat import raw_input

import dbConnection

# Executa o interogare SQL pentru a adauga in baza de date
def AdaugaCarte(titlu, autor, editura, an, pret, gen):
    sqlInsert = 'INSERT INTO carte values ("%s", "%s", "%s", "%s", "%s", "%s")' %  (titlu, autor, editura, an, pret, gen)
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
def MeniuAdaugaCarte():
    print("===============================")
    print("Adaugare Carte in baza de date:")
    print("===============================")
    titlu = raw_input("Introduceti titlul cartii: ")
    autor = raw_input("Introduceti autorul: ")
    editura = raw_input("Introduceti editura: ")
    an = raw_input("Introduceti anul aparitiei: ")
    pret = raw_input("Introduceti pretul: ")
    gen = raw_input("Introduceti genul cartii:\n - 1 - Beletristica, 2 - Stiinta, 3 - Comedie, 4 - Romantic, 5 - SF, 6 - Enciclopedie: ")
    if gen == "1":
        gen = "Beletristica"
    elif gen == "2":
        gen = "Stiinta"
    elif gen == "3":
        gen = "Comedie"
    elif gen == "4":
        gen = "Romantic"
    elif gen == "5":
        gen = "SF"
    elif gen == "6":
        gen = "Enciclopedie"
    else:
        print("Ati introdus informatii gresite!")
        raw_input("Apasati 'Enter' pentru a va intoarce la meniu.")
        return

    AdaugaCarte(titlu, autor, editura, an, pret, gen)