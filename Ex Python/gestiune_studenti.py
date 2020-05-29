class GestiuneStudenti:
        nume = None
        specializare = None
        anStudiu = None
        note = [None] * 10
 
        def __init__(self, nume, sp, an, note):
            self.nume = nume
            self.specializare = sp
            self.anStudiu = an
            self.note = note
 
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

        def setNota(self, index, n):
            if index <= len(self.note):
                self.note[index] = n
 
        def verificareRestantier(self):
            for i in self.note:
                if i < 5:
                    return self.nume

s = GestiuneStudenti("Andrei", "PABD", 1, [8, 10, 9])
s2 = GestiuneStudenti("Robert", "PABD", 2, [8, 9, 7])
s3 = GestiuneStudenti("Daniel", "INFO", 3, [10, 4, 9])
s.afisare()
s2.afisare()
s3.afisare()
s2.setSpecializare("EA")
s3.setAn(2)
s2.setNota(1, 4)
s.afisare()
s2.afisare()
s3.afisare()
restantieri = []
for i in [s, s2, s3]:
    r = i.verificareRestantier()
    if r:
        restantieri.append(r)
print("Restantieri:", restantieri)