class Optimizar:

    array=[]

    def inp(self):
        numero= int(input("Introduce un numero"))
        return numero


    def add(self, n):
        self.array.append(n)


    def media(self):
        suma = 0
        for i in self.array:
            suma += i
        m=suma/len(self.array)
        return m

