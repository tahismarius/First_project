# def print_hi(nume=True, prenume=None): # prenume si nume sunt paramertrii
#     if nume == 'Test' and prenume == 'None':
#         print('TEEEEST')
#         return nume + prenume
#     # return 'Hello'
#
#
# print(print_hi('Test', 'None'))

# def nr_nat(numar):
#     if numar >= 0:
#         return 'Numar natural'
#     else:
#         return 'Numar nenatural'
#
#
# rasp = nr_nat(-2)
# print(rasp)

# calculam impozitul pe masina
# cc = int(input('Introduceti capacitatea cilindrica'))
# impozit = None
#
#
# def calcul_impozit(hibrid_input, cc_input):
#     if hibrid_input:
#         return 10
#     elif cc_input < 1200:
#         return 75
#     elif cc_input > 1200 and cc_input < 1600:
#         return 125
#     elif cc_input > 1600 and cc_input < 2000:
#         return 200
#     else:
#         return 500
#
#
# impozit = calcul_impozit(False, cc)
# print(impozit) # 75
# impozit = calcul_impozit(True, 500)
# print(impozit) # 10
# impozit = calcul_impozit(False, 1599)
# print(impozit) # 125
# impozit = calcul_impozit(False, 1601)
# print(impozit) # 200


# cand am mai putina benzina de 15% in rezervor sa imi afiseze Warning

# REZERVOR = 50
# benz = float(input('Introduceti benzina ramasa'))
#
# def benzina_ramasa(benzina_input):
#     procentaj_benz = benzina_input / REZERVOR * 100
#     if procentaj_benz <= 15:
#         print('Warning')
#     elif procentaj_benz > 100:
#         print(f'Nu se poate sa avem mai multa bezina decat capactitatea de {REZERVOR} litrii a rezervorului')
#     else:
#         print('Mai aveti destula benzina')
#     return procentaj_benz
#
#
#
#
# benz_ramasa = benzina_ramasa(benz)
# print(f'mai ai {benz_ramasa}% benzina ramasa')



# functii din alte fisiere
from helper import suma
from helper import produs


def produs2():
    a = int(input("introdu a"))
    b = int(input("introdu b"))
    print(produs(a, b))
    print(suma(a, b))


produs2()



