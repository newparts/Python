import random
class Student:
    nrDiscipline = 3 # variabila de clasa

    def __init__(self, nume, sp, an):
        self.nume = nume
        self.specializare = sp
        self.anStudiu = an

    def afisare(self):
        print("Nume:", self.nume)
        print("Specializare:", self.specializare)
        print("An studiu:", self.anStudiu)
        print("Note:", self.note)

    def setNume(self, n):
        self.nume = n

    def setSpecializare(self, sp):
        self.specializare = sp
 
    def setAn(self, a):
        self.anStudiu = a

    def setNote(self, note):
        self.note = note

    def adaugaNote(self, nota):
        self.note.append(nota)
 
    def verificareRestantier(self):
        if len(self.note) < self.nrDiscipline:
            return self.nume # daca studentul nu are suficiente note va fi considerat restantier
        for i in self.note:
            if i < 5:
                return self.nume # daca studentul are o nota sub 5 va fi considerat restantier

studenti = [Student("Andrei", "PABD", 1), Student("Robert", "Cadastru", 2), Student("Daniel", "INFO", 3)]

for i in studenti:
    nrNote = random.randrange(1, Student.nrDiscipline+1) # numar random de note ale studentului ( maxim numarul disciplinelor )
    note = []
for j in range(0, nrNote):
    note.append(random.randrange(1, 10)) # adaugarea notelor random ale studentului, bazat pe numarul notelor
 
    i.setNote(note)
    i.afisare()
studenti[0].setSpecializare("EA")
studenti[1].setAn(4)
for i in studenti:
    i.afisare()
    restantieri = []
for i in studenti:
    r = i.verificareRestantier()
    if r:
        restantieri.append(r)
print("Restantieri:", restantieri)