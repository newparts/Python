class Student:
     def __init__(self, num, spec, an, nota):
        self.nume = num
        self.specializare = spec
        self.anStudiu = an
        self.note = nota
 
        def afisare_student(self, nrNota):
            print('Nume: ' + str(self.nume))
            print('Specializare: ' + str(self.specializare))
            print('An: ' + str(self.anStudiu))
            if nrNota >= len(self.note):
                print('Nota: ' + str(self.note[len(self.note) - 1]))
            else:
                print('Nota: ' + str(self.note[nrNota]))
            print('\n')
 
        def schimbare_proprietati(self, proprietate, nrNota = 0):
            if proprietate == 'n':
                self.nume = input('Noul nume pentru ' + self.nume + ': ')
            elif proprietate == 's':
                self.specializare = input('Noua specializare pentru ' + self.nume + ': ')
            elif proprietate == 'an':
                self.anStudiu = input('Noul an de studiu pentru ' + self.nume + ': ')
            elif proprietate == 'no':
                if nrNota >= len(self.note) or nrNota == 0:
                    self.note[len(self.note) - 1] = int(input('Noua nota pentru: ' + self.nume + ': '))
                else:
                    self.note[nrNota] = int(input('Noua nota pentru: ' + self.nume + ': '))
 
        def este_restantier(self):
            for i in range(0, len(self.note)):
                if self.note[i] < 5:
                    print(self.nume + ' este restantier!')
                    return
            print(self.nume + ' nu este restantier!')

studenti = [Student('Stef Alin', 'PABD', '1', [10, 7, 9]),
            Student('Tibea Laurentiu', 'PABD', '1', [10, 6, 9]),
            Student('Bancila Mihai', 'PABD', '1', [8,4,9])]

for i in range(0,3):
    studenti[i].afisare_student(1)
            
studenti[1].schimbare_proprietati('s')
studenti[0].schimbare_proprietati('an')

for i in range(0,3):
    studenti[i].afisare_student(1)
for i in range(0,3):
    studenti[i].este_restantier()