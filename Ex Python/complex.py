class Complex:
 def __init__(self, real, imaginar):
    self.r = real
    self.i = imaginar
 def aflare_semn(self, im):
    if im < 0:
        im = im * -1
        semn = '-'
    else:
        semn = '+'
    return semn, im
 def inmultire(self, nr_complex):
    re = (self.r * nr_complex.r - self.i * nr_complex.i)
    im = (self.r * nr_complex.i + nr_complex.r * self.i)
    print('Inmultire: ' + str(re) + ' ' + self.aflare_semn(im)[0] + '' + str(self.aflare_semn(im)[1]) + 'i')
 def adunare(self, nr_complex):
     re = (self.r + nr_complex.r)
     im = (self.i + nr_complex.i)
     print('Adunare : ' + str(re) + ' ' + self.aflare_semn(im)[0] + ' ' + str(self.aflare_semn(im)[1]) + 'i')
 def scadere(self, nr_complex):
    re = (self.r - nr_complex.r)
    im = (self.i - nr_complex.i)
    print('Scadere : ' + str(re) + ' ' + self.aflare_semn(im)[0] + ' ' + str(self.aflare_semn(im)[1]) + 'i')
z1 = Complex(-2, -5)
z2 = Complex(-3, -6)
z1.inmultire(z2)
z1.adunare(z2)
z1.scadere(z2)