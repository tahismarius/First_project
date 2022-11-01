# #ex1
# note_muzicale = ['do','re', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# print(note_muzicale[::-1])
# note_muzicale.reverse()
# print(note_muzicale)
#
# for x in note_muzicale:
#     print(x)
#
# #ex2
#
# print(len('do'))

# #ex3
# list1 = [3,1,0,2]
# list2 = [6,5,4]
# list3 = list1+ list2
# print(list3)
# list4=list1.__add__(list2)
# print(list4)

#ex4
# c=[3,1,0,2, 6,5,4]
# d=c.pop(2)
# print(c)
# print(d)

#ex5

# c=[3,1,0,2, 6,5,4]
# d=c.copy()
# d.clear()
# print(d)
# if c !=d:
#     print(f'lista nu este goala')
# else:print(f'Lista  este goala')
#
# #ex6
# c=[3,1,0,2,6,5,4]
# del c[0:7]
# print(c)

# #ex7
# c=[3,1,0,2, 6,5,4]
# d=c.copy()
# d.clear()
# print(d)
# if c ==d:
#     print(f'lista nu este goala')
# else:print(f'Lista  este goala')
#
# #ex8
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())

# # #ex9
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1)
# x=dict1.get('Ana')
# print(f'Ana a luat nota {x}')
# y=dict1.get('Gigel')
# print(f'Gogel a luat nota {y}')
# z=dict1.get('Dorel')
# print(f'Dorel a luat nota {z}')
#
# #ex10
# dict1.update({"Dorel" : '6'})
# print(dict1)
#
# #ex11
# dict1.pop('Gigel')
# dict1.update({'Ionica': '9'})
# print(dict1)

# #ex12
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# print(zile_sapt)
# zile_sapt.add('lunia')
# print(zile_sapt)
#
# #ex13
# if weekend.issubset(zile_sapt)==True:
#     print(f'wekend este subset de zile sapt')
# else:print(f'wekend nu este subset de zile sapt')
#
# #ex14
# m=zile_sapt.difference(weekend)
# print(m)
#
# i=zile_sapt.intersection(weekend)
# print(m)