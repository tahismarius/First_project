#ABSTRACTION

from abc import ABC, abstractmethod


class FormeGeometrice(ABC):
     Pi =3.14


     @abstractmethod
     def aria(self):
         raise NotImplementedError


     def descript_class(self):
         print("cel mai probabil am colturi")


#INHERITANCE

class Patrat(FormeGeometrice):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura
     
    @latura.getter
    def latura(self,latura):
         print(f'Getter : Latura este {self.__latura}')
         
    @latura.setter
    def latura (self, latura):
         print(f'Setter:Noua latura este {latura}')
         self.__latura=latura

    @latura.deleter
    def latura(self):
         print(f'Delter:Am sters latura')
         self.__latura= None

    def aria(self,aria_latura=None):
        aria_latura = self.__latura *self.__latura
        print(f'Aria este {aria_latura}')


class Cerc(FormeGeometrice):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua raza a cercului este {raza}')

    @raza.deleter
    def raza(self):
        print('Am sters raza cercului')
        self.__raza=None

    def aria(self,aria_cerc):
        aria_cerc= self.Pi * (self.__raza * self.__raza)

def describe():
    print(f'Eu nu am colturi')

patrat= Patrat(10)
patrat.descript_class()
patrat.aria()
describe()

cerc= Cerc(27)
cerc.descript_class()
cerc.aria()
cerc.raza()
describe()



