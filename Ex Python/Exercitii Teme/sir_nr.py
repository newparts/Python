class Sir:
     def __init__(self, s):
        self.sir = s
 
        def calculare_maxim(self):
            max = self.sir[0]
            for i in range(1,len(self.sir)):
                if self.sir[i] > max: max = self.sir[i]
            return max
 
        def calculare_minim(self):
            min = self.sir[0]
            for i in range(1,len(self.sir)):
                if self.sir[i] < min: min = self.sir[i]
            return min
 
        def caluclarea_mediei(self):
            medie = 0
            for i in range(0,len(self.sir)):
                medie += self.sir[i]
            return medie/len(self.sir)

        def __bubble_sort(self):
            flag = 1
            i = 0
            aux = 0
            while flag == 1:
                flag = 0
                for i in range (0,len(self.sir) - 1):
                    if self.sir[i] > self.sir[i+1]:
                        aux = self.sir[i]
                        self.sir[i] = self.sir[i+1]
                        self.sir[i+1] = aux
                        flag = 1
            return self.sir

        def calcularea_medianei(self):
            self.sir = self.__bubble_sort()
            if len(self.sir) % 2 == 0:
                mediana = (self.sir[len(self.sir) / 2 - 1] +
            self.sir[len(self.sir) / 2 + 1]) / 2
            else:
                mediana = self.sir[int((len(self.sir) - 1) / 2)]
                return mediana

sir = [8,4,3,9,6,1,2]
array = Sir(sir)

print('Maxim: ' + str(array.calculare_maxim()))
print('Minim: ' + str(array.calculare_minim()))
print('Media: ' + str(array.caluclarea_mediei()))
print('Mediana: ' + str(array.calcularea_medianei()))