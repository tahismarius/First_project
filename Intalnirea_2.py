
# acelasi string de mai sus
# folositi un assert ca sa verificati daca acest string contine doar numere


# tipuri de date : string, int, bool, float

# my_str = 'Iuliu-Matei Oltean este numele meu complete'
#
# my_str2 = '78945612634569984984'
# print(type(my_str))
# print(my_str)
#
#
# x = my_str.replace('e', 'T', 3)
# print(x)
#
# print(my_str.replace('e', 'T', 3))
# print(my_str.isdigit())
# print(my_str.endswith('t'))

# import os # import modulul ...
#
# if os.path.exists("C:\Program Files (x86)\Overwolf"):
#     print("Path-ul exista")
# else:
#     print("Path-ul nu exista")


# x = input("Introduceti user ")
# y = input("Introduceti parola ")
#
# lung_parola = (len(y))
# print(lung_parola)
# obf = lung_parola * '*'
#
# print(f'Userul este {x}, \nParola lui este {obf} \nSi are \n{lung_parola} caractere')

# numele_meu = 'Matei'
# prenumele_meu = 'Oltean'
#
# x = len(numele_meu + prenumele_meu)
#
# print(x)
#
# print(f'{numele_meu} {prenumele_meu} are {x} caractere')

# x = input('Intorduceti parola')
# if len(x) < 8:
#     print("Parola nu are lungimea corespunzatoare")
# else:
#     print("Parola are lungimea corespunzatoare")

# opeatori de atribuire

# x = 5
# x = x + 10
# x += 10
#
# x -= 9
# x *= 2
# x /= 32
#
# print(int(x))
#
#
# y = 10
# z = 311 % 3
# print(z)
#
# p = 1000 ** 3
# print(p)
#
# k = 50
# print((k // 6) + p + z + x)


# x = 'String'
# y = 'String'
#
# # if len(x) == len(y):
# #     print("True")
# # else:
# #     print("False")
#
# assert len(x) != len(y)
# print('True')
# a = '9999'
# if a == 'String':         # daca conditia este adevarata, intra pe prima "usa"
#     print("Adevarat")
# else:                     # altfel intra pe cea de-a doua "usa" - conditia nefiind adevarata
#     print("Fals")

# operatori logici = or, and , not

# a = '999'
# if a == '9999' or len(a) == 3 and (4 - 1 == 3):
#     if a.isdigit():
#         print('1')
#     else:
#         print('2')
# else:
#     print('Whatever')
#
# # 1.False or 2.False si 3.True = False - print whatever
# # 1.True or 2.False si 3.True = True - print 1
# # 1.False or False si 3. True = False  - print whatever
#
# # (False sau False) si True = False = print Whatever
# # (True sau False) si True = True = print 1
# # (True sau False) si False = False = print whatever
# # (False sau False) si False = False = print whatever
# # (True sau True) si True = True = print 1
# # (False sau True) si True = True = print 1


# a = input("Introduceti optiunea")
# x = len(a)
# y = a.upper()
#
# if x == 1:
#     print(f'Ati introdus {a.upper()}')
# elif x == 2:
#     print(f'X are lungimea {x}')
# elif x == 3:
#     print(f'Bla bla {a.lower()}')
# elif x == 4:
#     print(f'X are lungimea {x}')
# elif x == 5:
#     print(f'X are lungimea {x}')
# elif x == 6:
#     print(f'X are lungimea {x}')
# else:
#     print(f'Nu exista optiunea {a}')

# x = input('Ce doresti sa afli?\n Pentru IF apasa 1\n Pentru ELSE apasa 2\n Inputul tau=')
#
# if x == '1':
#     print('Sintagma de IF vine din engleza de la flow control si inseamna ca exercitam un control\n in structura codului.')
# elif x == '2':
#     print('ELSE inseamna altfel si controleaza flow mergand pe varianta falsa')
# else:
#     print(f'Ne pare rau dar nu avem disponbila optiunea cu numarul {x}')
# n = input('Introduceti un numar')
# m = int(n)
# print(m)
# if m >= 0:
#     print("N este natural")
# else:
#     print("N nu este numar natural")

# x = input('Introdu N')
# if x == '1':
#     print(f"Ati introdus valoarea {x} \n Please introduce another value:")
#     y = input("Introduce the new value ")
#     if y == '2':
#         print(f"Ati introduSS valoarea {y}")
#     elif y == '3':
#         print(f"Ati introduSSS valoarea {y}")
#     elif y == '4':
#         print(f"Ati introduSSSS valoarea {y}")
#     else:
#         print(f"Ati introduSSSSS valoarea {y}")
#     z = input("Introduce the new value ")
#     if z < "5":
#         print("salut")
#     else:
#         print("la revedere")
# else:
#     print(f"Valoarea introdusa este foate mare {x}")
