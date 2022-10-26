# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# -	Efectuam schimbarea
# -	Stergem jucatorul scos din lista
# -	Adaugam jucatorul intrat
# -	Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# -	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# -	Afisati ‘mai aveti z schimbari’

# SCHIMBARI_MAX = 3
# schimbari_ramase = SCHIMBARI_MAX  #j6, j7, j8
# echipa = {'j1', 'j2', 'j3', 'j5', 'j4'}
# jucator_out = input('introduceti un jucator care sa iasa')
# jucator_in = input('introduceti un jucator sa intre ')

#
# if jucator_out in echipa and schimbari_ramase > 0:
#     if jucator_in in echipa:
#         print('Nu putem face schimbarea')
#     else:
#         echipa.remove(jucator_out)
#         echipa.add(jucator_in)
#         schimbari_ramase = schimbari_ramase - 1
#         print(f'Am introdus {jucator_in}')
#         print(f'Am scos {jucator_out}')
#         print(f'echipa actuala este {echipa}')
#         print(f'Mai avem {schimbari_ramase} schimbari')
# else:
#     if schimbari_ramase <= 0:
#         print(f'Nu mai avem schimbari')
#     else:
#         print(f'Nu putem face schimbarea pentru ca jucatorul {jucator_out} este deja in teren')





# while / while else

# i = 0
# while i <= 1100:
#     print(i)
#     if i < 1000:
#         print('Bravo')
#     else:
#         print('Nu e bine')
#     i = i + 1
#     i = i + 10
#     i = i + 99
# else:
#     print('Am ajuns la limita')

# for /for else

# for i in range(10, 100, 5):
#     print(i)
# else:
#     print('Am ajuns la limita')

# mancare = ['hamburger', 'senvis', 'lapte', 'oua', 'dulceata', 'hamburger', 'hamburger', 'hamburger']
# for tip_mancare in mancare:
#     if tip_mancare == 'hamburger':
#         nr_ham = mancare.count('hamburger')
#         print(f'Clientii au cumparat un numar de {nr_ham} hamburgeri')
#     elif tip_mancare == 'oua':
#         nr_oua = mancare.count('oua')
#         print(f'Numarul de oua vandut este {nr_oua}')

# break
# for i in range(999):
#     if i == 4:
#         break
#     print(f'{i} dupa break')


#continue
# for i in range(5):
#     if i == 2:
#         print(f"Am ajuns la doi, sarim peste el")
#         continue
#     print(f'{i}')

