from math import sqrt
from math import pi

# triunghi

class Triunghi:
    def __init__(self, cateta1, cateta2, ipotenuza):
        self.c1 = cateta1
        self.c2 = cateta2
        self.ip = ipotenuza

    def perimetru(self):
        return self.c1 + self.c2 + self.ip

    def arie(self):
        pass

class Isoscel(Triunghi):
    def __init__(self, cateta1, cateta2, ipotenuza):
        Triunghi.__init__(self, cateta1, cateta2, ipotenuza)
    
    def perimetru(self):
        return Triunghi.perimetru(self)

    def arie(self):
        self.med = sqrt(self.c1 ** 2 - (self.ip / 2) ** 2)
        return (self.ip * self.med) / 2

class Echilateral(Triunghi):
    def __init__(self, cateta1, cateta2, ipotenuza):
        Triunghi.__init__(self, cateta1, cateta2, ipotenuza)
 
    def perimetru(self):
        return Triunghi.perimetru(self)
 
    def arie(self):
        return (self.c1 ** 2 * sqrt(3)) / 4

# patrulater

class Patrulater:
    def __init__(self, latura1, latura2):
        self.l1 = latura1
        self.l2 = latura2
    
    def perimetru(self):
        return 2 * (self.l1 + self.l2)
 
    def arie(self):
         pass

class Patrat(Patrulater):
    def __init__(self, latura1, latura2):
        Patrulater.__init__(self, latura1, latura2)
 
    def perimetru(self):
        return Patrulater.perimetru(self)
    
    def arie(self):
        return self.l1 * self.l2

class Dreptunghi(Patrat):
    def __init__(self, latura1, latura2):
        Patrat.__init__(self, latura1, latura2)
 
    def perimetru(self):
        return Patrat.perimetru(self)
 
    def arie(self):
        return self.l1 * self.l2

class Paralelogram(Patrulater):
    def __init__(self, latura1, latura2, inaltime):
        Patrulater.__init__(self, latura1, latura2)
        self.ina = inaltime
 
    def perimetru(self):
        return Patrulater.perimetru(self)
 
    def arie(self):
        if self.l1 >= self.l2: return self.l1 * self.ina
        else: return self.l2 * self.ina

class Romb(Paralelogram):
    def __init__(self, latura1, latura2, inaltime):
        Paralelogram.__init__(self, latura1, latura2, inaltime)
 
    def perimetru(self):
        return Paralelogram.perimetru(self)
 
    def arie(self):
        return Paralelogram.arie(self)

# cercul

class Cerc:
    def __init__(self, raza):
        self.r = raza

    def perimetru(self):
        return 2 * pi * self.r
 
    def arie(self):
        return pi * self.r ** 2

tI = Isoscel(5,5,6)
tE = Echilateral(5,5,6)
p = Patrat(4,4)
d = Dreptunghi(4,6)
pp = Paralelogram(3,5, 2)
c = Cerc(5)

print('Perimetru T Isoscel: ' + str(tI.perimetru()))
print('Arie T Isoscel: ' + str(tE.perimetru()))
print('Perimetru T Echilateral: ' + str(tI.arie()))
print('Arie T Echilateral: ' + str(tE.arie()))
print('Perimetru Patrat: ' + str(p.perimetru()))
print('Arie Patrat: ' + str(p.arie()))
print('Perimetru Dreptunghi: ' + str(d.perimetru()))
print('Arie Dreptunghi: ' + str(d.arie()))
print('Perimetru Paralelogram: ' + str(pp.perimetru()))
print('Arie Paralelogram: ' + str(pp.arie()))
print('Perimetru Cerc: ' + str(c.perimetru()))
print('Arie Cerc: ' + str(c.arie()))
