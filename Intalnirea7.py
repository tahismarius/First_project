#Exceptii
# print('Inainte de diviziune')
#
# try:
#     list = [1, 2, 3]
#     list[6]
# except IndexError as e:
#     print(e)
#
# print('Dupa divziune')

# x = 'hello'
#
# if not type(x) is int:
#     raise TypeError('Folsiti doar tipul int')


# try:
#     x = 10
#     rez = x / 0
#     print(rez)
# except TypeError:
#     print('Eroare tip')

# try:
#     print('Hello')
# except:
#     print('Test1')
# else:
#     print('Test2')

# try:
#     #x = 'salut'
#     print(x)
# except:
#     print('Gresit')
# finally:
#     print('Am ajuns la final')

# Inheritance - mostenire

# class Chef:
#     tava = 1
#     def make_salad(self):
#         print('Pot sa gatesc salata')
#
#     def make_soup(self):
#         print('Pot sa gatesc supa')
#
# class Chef2:
#     tava2 = 1
#     def make_salad2(self):
#         print('Pot sa gatesc salata2')
#
#     def make_soup2(self):
#         print('Pot sa gatesc supa2')
#
#
# class ChefJaponez(Chef, Chef2):
#
#     def make_sushi(self):
#         print('Pot sa gatesc sushi')
#
#
# class ChefItalian(Chef):
#
#     def make_pizza(self):
#         print('Pot sa gatesc pizza')
#
#
# std_jap = ChefJaponez()
# std_jap.make_salad()
# std_jap.make_soup()
# std_jap.make_sushi()
# #std_jap.tava
#
# std_it = ChefItalian()
# std_it.make_salad()
# std_it.make_soup()
# std_it.make_pizza()
# #std_it.tava


# Polymorphism

# print(len('testrewtdsfgsdfgsdfg'))
#
# print(len([1, 2, 3, 10, 20, 30]))


# def adunare(x, y=0, z=0):
#     print(x)
#     print(y)
#     print(z)
#
#     return x + y + z
#
#
# print('Adunarea zero', adunare(4, 67))
#
#
# print('Prima adunare', adunare(2, 3))
#
# print('A doua adunare', adunare(2, 3, 4))

# class Romania:
#     def language(self):
#         print('Romaneste')
#
#     def danseaza(self):
#         print('Dans romanesc')
#
# class Italia:
#     def language(self):
#         print('Italiana')
#
#     def danseaza(self):
#         print('Dans italian')
#
# class Brazilia:
#     def language(self):
#         print('Portrugheza')
#
#
#     def danseaza(self):
#         print('Dans portughez')
#
#
# x_ro = Romania()
# x_it = Italia()
# x_br = Brazilia()
#
#
# for tara in (x_ro, x_br, x_it):
#     tara.language()
#     tara.danseaza()

# exemplu de polimorfism + mostenire
# class Pasari:
#
#     def descriere(self):
#         print('Exista mai multe specii de pasari')
#
#
#     def zboara(self):
#         print('Majoritatea pasarilor pot sa zboare')
#
#
# class Bufnita(Pasari):
#
#     # def descriere(self):
#     #     print('Bufnitele sunt pasari nocturne')
#
#     def zboara(self):
#         print('Bufnitele pot sa zbura')
#
#
# class Pinguin(Pasari):
#
#     # def descriere(self):
#     #     print('Pinguinii traiesc la Polul Sud')
#
#     def zboara(self):
#         print('Pinguinii nu pot sa zboare')
#
# x_pasari = Pasari()
# x_bufnita = Bufnita()
# x_pinguin = Pinguin()
#
#
# x_pasari.descriere()
# x_pasari.zboara()
# print(' ')
# x_bufnita.descriere()
# x_bufnita.zboara()
# print(' ')
# x_pinguin.descriere()
# x_pinguin.zboara()



# Abstract class

# from abc import ABC, abstractmethod
#
# class Poligon(ABC):
#
#     @abstractmethod
#     def nr_de_laturi(self):
#         pass
#
#     @abstractmethod
#     def perimetru(self):
#         """
#         in aceasta clasa se va colcula si afisa perimetrul
#         """
#         pass
#
#     @abstractmethod
#     def arie(self):
#         pass
#
#     @abstractmethod
#     def test(self):
#         pass
#
#
# class Poligon2(ABC):
#
#     @abstractmethod
#     def test2(self):
#         pass
#
#
# class Triunghi(Poligon, Poligon2):
#     def nr_de_laturi(self):
#         print('Am 3 laturi')
#
#     def perimetru(self):
#         print('Perimetrul trihunghiului e suma celor 3 laturi')
#
#     def arie(self):
#         pass
#
#     def test(self):
#         pass
#
#     def test2(self):
#         pass
#
#
# class Patrat(Poligon):
#     def nr_de_laturi(self):
#         print('Patratul are 4 laturi')
#
#     def perimetru(self):
#         pass
#
#     def arie(self):
#         pass
#
#     def test(self):
#         pass
#
#
# class Hexagon(Poligon):
#     def nr_de_laturi(self):
#         print('Hexagonul are 6 laturi')
#
#     def perimetru(self):
#         pass
#
#     def arie(self):
#         pass
#
#     def test(self):
#         pass
#
#
# R = Triunghi()
# R.nr_de_laturi()
# R.perimetru()
#
# F = Patrat()
# F.nr_de_laturi()
# F.perimetru()
#
# G = Hexagon()
# G.perimetru()
# G.nr_de_laturi()


#Encapsulation


# class Counter:
#
#     def __init__(self):
#         self.__current = 0
#
#     def creste(self):
#         self.__current += 1
#
#     def valoare(self):
#         return self.__current
#
#     def reset(self):
#         self.__current = 0
#
#
# counter = Counter()
# counter.creste()
# counter.creste()
# counter.current = 999
# counter.creste()
# counter.reset()
# counter.creste()
# counter.creste()
# counter.creste()
# counter.creste()
# counter.reset()
# counter.creste()
#
#
# print(counter._Counter__current)



# print(counter.valoare())


# class Nume:
#
#     nume = None
#     prenume = None
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#
#
#     def __nume_complet(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         print(f'Nume complet {self.nume}{self.prenume}')
#
#     def descrie(self):
#         return self.__nume_complet(nume='Matei', prenume='Oltean')
#
#
# n = Nume('Matei', 'Oltean')
#
# print(n.descrie())


# class Persoana:
#
#     def __init__(self,  varsta=0):
#         self.varsta = varsta
#
#     #getter method
#     def get_varsta(self):
#         print(f'Varsta este {self.varsta}')
#
#     #setter method
#     def set_varsta(self, x):
#         self.varsta = x
#
#     #deleter
#     def delete_varsta(self):
#         self.varsta = None
#
# obiect = Persoana()
#
# #setting varsta
# obiect.set_varsta(21)
# obiect.delete_varsta()
# #obiect.get_varsta()
# obiect.set_varsta(45)
# obiect.get_varsta()

