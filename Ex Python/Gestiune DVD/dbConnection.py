# dbConnection.py

# Cele mai importante module Python DB API

# MySQL - MySQLdb
# PostgreSQL - psycopg(2)
# SQLite - sqlite3
# Oracle - oracle
# MS SQL server - adodbapi

import pymysql

# variabile pentru accesul la baza de date
HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'test1'

def CreeazaConexiune():
    # creeaza o conexiune la baza de date
    try:
        #db = pymysql.connect(host=HOST, user=USER, db=DATABASE)
        db = pymysql.connect(host='localhost', port=3306, user='root', password='', db='test1')

        # print "Conexiunea la baza de date s-a realizat cu succes!"
        return db
    except Exception as e:
        print("Eroare la conexiunea cu baza de date! - ", e)

def CreeazaBazaDeDate():
    # creeaza baza de date
    db = CreeazaConexiune()
    if db == None:
        try:
            db = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD)
            db.cursor().execute('CREATE DATABASE ' + DATABASE)
        except Exception as e:
            print("Eroare la crearea bazei de date!", e)


def CreeazaTabela():
    # creeaza tabel
    db=CreeazaConexiune()
    # pentru a executa interogari asupra bazei de date este nevoie de un obiect de tip cursor
    cursor=db.cursor()
    cursor.execute('USE ' + DATABASE)

    cursor.execute("""        
        CREATE TABLE dvd(        
        titlu Varchar(100),        
        actor_principal VARCHAR(100),        
        actor_secundar  VARCHAR(100),        
        an INT,        
        gen VARCHAR(100)          
        )        
        """)

    db.commit()
    cursor.close()
    db.close()

CreeazaConexiune()