# breakout rooms code - functie care determina daca numele este de baiat sau fata
#
# nume_exceptii_baieti = ['Horea', 'Mircea', 'Romica', 'Mihai']
# nume_exceptii_fete = ['Carmen', 'Beatrice']
#
# #vocale = ["a", "e", "i", "o", "u", "ă", "î"]
#
#
# def nume_baiat_sau_fata(nume=" "):
#     if (nume[len(nume)-1] == 'a' or nume in nume_exceptii_fete) and nume not in nume_exceptii_baieti:
#         print("Este nume de fata")
#     else:
#         print("Este nume de baiat")
#
#
# nume_baiat_sau_fata('Romica')
#
# exc_fete = []
# exc_baieti = []
#
#
# def nume_fete(nume):
#     if nume.endswith('a') or nume == 'Carmen':
#         print("Acest nume este de fata.")
#     else:
#         print("Acest nume este de baiat")
#
#
# nume_fete("Carmen")
#
#
# conceptul de clasa, constructor, metode, obiecte

# import os
# class ScripTA:
#     fisier: None
#     folder: None
#
#     #constructor
#     def __init__(self, fisier, folder):
#         self.fisier = fisier
#         self.folder = folder
#
#     #metode
#     def verificare_folder(self):
#         if os.path.exists(self.fisier):
#             print(f'Iti poti desfasura munca pentru ca folderul {self.folder} exista')
#         else:
#             print('Nu am gasit folderul specificat')
#
#     def verificare_fisier(self):
#         if os.path.exists('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt'):
#             print('Fisierul exista')
#         else:
#             print('Fisierul nu exista')
#
#     def creare_fisier(self):
#         if os.path.exists('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt'):
#             print('Fisierul exista')
#         else:
#             f = open('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt', 'w')
#             f.close()
#             print('Fisierul a fost doar creat')
#
#     def editare_fisier(self):
#         if os.path.exists('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt'):
#             f = open('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt', 'w')
#             f.write('Acesta este primul edit')
#             f.close()
#             print('Fisierul a fost editat')
#         else:
#             print('Fisierul nu exista')
#
#     def redenumire_fisier(self):
#         if os.path.exists('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt'):
#             os.rename('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt',
#                       'C:\\Users\\oltea\\Desktop\\testare_automata\\test_file_automated.txt')
#             print('Fisierul a fost redenumit')
#         elif not os.path.exists('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt'):
#             f = open('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt', 'w')
#             f.close()
#             os.rename('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt',
#                       'C:\\Users\\oltea\\Desktop\\testare_automata\\test_file_automated.txt')
#             print('Fisierul creat si redenumit')
#         else:
#             print('Nu exista fisierul dorit')
#
#
#     def stergere_fisier(self):
#         if os.path.exists('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt'):
#             os.remove('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt')
#             print('Fisierul a fost sters')
#         else:
#             print('Nu gasim fisierul dorit')
#
#
# scr1 = ScripTA('C:\\Users\\oltea\\Desktop\\testare_automata\\test_file.txt',
#                'C:\\Users\\oltea\\Desktop\\testare_automata')
#
# scr1.verificare_folder()
# scr1.editare_fisier()
# scr1.creare_fisier()
# scr1.editare_fisier()
# scr1.redenumire_fisier()
# scr1.stergere_fisier()
# scr1.verificare_fisier()

# from helper import suma
# print(suma(21, 22))
#
from helper import Persoana

pers1 = Persoana('Matei', 'Oltean', 5)
print(pers1.descrie())
print(pers1.ani())
pers2 = Persoana('Andrei', 'Test', 25)
print(pers2.descrie())
print(pers2.ani())
#
# scr2 = scr1
#
# scr2.verificare_fisier()
# scr2.creare_fisier()

