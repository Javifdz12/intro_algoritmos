#conociendo base y altura
base=float(input("¿cual es la base del triangulo?"))
altura=float(input("¿cual es la altura del triangulo?"))
def area_triangulo(base,altura):
    return (base*altura)/2
print(f'el area del triangulo es {area_triangulo(base,altura)}')

#conociendo 2 lados y angulo entre lados
import numpy as np
import math
def seno(a):
    a=math.radians(a)
    return math.sin(a)

class triangulo1:
    def __init__(self,lado1,lado2,angulo_entre_lados):
        self.lado1=lado1
        self.lado2=lado2
        self.angulo_entre_lados=angulo_entre_lados
    def area(self):
        return ((self.lado1*self.lado2)/2)*seno(self.angulo_entre_lados)
class triangulo2:    
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return (self.base*self.altura)/2
        
triangulo1=triangulo1(4,3,90)
triangulo2=triangulo2(4,3)
triangulo1.area()
triangulo2.area()