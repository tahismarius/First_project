# list1 = ["abc", 'b23', 'crue', 'dalse', 'eanana', "fortocala", "gortocala", 'h.0']
# print(list1)
# print(len(list1))
# print(list1)
#
# print(list1[::-1])

# list1[0] = 'DEF'
# print(list1)

# list1[0:3] = ['ADI', 499, False]
# print(list1)

# list1.insert(4, 'banana')
# print(list1)
# print(len(list1))

# list1.append('camion')
# print(list1)
# print(len(list1))

# list1.remove('banana')
# print(list1)
# print(len(list1))
#
# list1.pop()
# print(list1)
# print(len(list1))
#
# del list1[4]
# print(list1)
# print(len(list1))
#
# list1.clear()
# print(list1)

# for x in range(len(list1)):
#     print(list1[x])

# x = 0
# while x < len(list1):
#     print(list1[x])
#     x += 1
# [print(x) for x in list1]
# list1 = ["ala", 'ala', 'ala', 'bala', 'portocala', "fortocala", "gortocala", 'h.0']
# print(list1)
# list1.insert(4, 'banana')
# list1.append('camion')
# list1.sort(reverse=True)
# print(list1)

# list2 = list1.copy()
# print(list2)
#
# list3 = list(list1)
# print(list3)

# list2 = ['ala', 'bala', 'portocala']
# print(list2)
#
# list3 = list1 + list2
# print(list3)
#
# x = list3.count('ala')
# print(x)

# string = 'Coral is either the stupidest animal or the smartest rock'
# x = string.()
# print(x)
#
# list4 = ['1', '2', '3']
# list3.extend(list4)
# print(list3)

# fruits = (True, 'portocale', 3.0, 'cirese')
# print(fruits)
# print(fruits[1])
# x = list(fruits)
# print(x)
# x[0] = 'kiwi'
# fruits = tuple(x)
# print(fruits)
# fruits2 = ('cirese',)
# fruits3 = fruits + fruits2
# print(fruits3)
#
# x = fruits3.count('cirese')
# print(x)
#
# y = fruits3.index('kiwi')
# print(y)
#
# print(f'Am un cos plin cu {fruits[1]}')

# setul1 = {'mar', 'banana', 'cireasa'}
# # print(setul1)
# # print(len(setul1))
#
# # for x in setul1:
# #     print(x)
#
# setul1.add('pineapple')
# # print(setul1)
# setul1.remove('pineapple')
# # print(setul1)
#
# setul2 = {'mar', 'cartof', 'cireasa', 'test', 'alin', 'verde'}
#
# setul3 = setul1.union(setul2)
# # print(setul3)
#
# setul1.update(setul2)
# print(setul1)
#
# x = setul1.difference(setul2)
# print(x)
#
# setul2.discard('cartof')
# print(setul2)
#
# setul2.pop()
# print(setul2)
#
# setul3 = {'a', 'b', 'c'}
# setul4 = {'f', 'g', 'h', 'a', 'b', 'c'}
# x = setul3.issubset(setul4)
# print(x)
#
# setul5 = {'f', 'g', 'h', 'a', 'b', 'c'}
# setul6 = {'a', 'b', 'c'}
# y = setul5.issuperset(setul6)
# print(y)

dictionar1 = {'nota': '10', 'nume': 'Matei', 'clasa': '9'}
print(dictionar1)
print(len(dictionar1))
print(dictionar1['nume'])
x = dictionar1.get('nota')
print(x)
y = dictionar1.keys()
print(y)
z = dictionar1.values()
print(z)

dictionar1['nota'] = 7
print(dictionar1)
dictionar1.update({'nota': '11'})
print(dictionar1)
dictionar1['materie'] = 'matematica'
print(dictionar1)
dictionar1.update({'medie': '7.85'})
print(dictionar1)
# dictionar1.pop('medie')
# print(dictionar1)
# dictionar1.popitem()
# print(dictionar1)
# del dictionar1['nota']
# print(dictionar1)
#del dictionar1 - sterge dictionarul

# dictionar1.clear()
# print(dictionar1)

for x in dictionar1:
    print(x)       # printeaza cheile

for y in dictionar1:
    print(dictionar1[y])   # printeaza cheile

dict2 = dictionar1.copy()
print(dict2)

dict3 = dict(dict2)
print(dict3)


familie = {'copil1': {'Index_zero': 'Matei', 'an': '1990'},
           'copil2': {'123': 'Andrei', 'an': '1991'},
           'copil3': {'456': 'Andrei', 'an': '1991'}
           }
print(familie)
x = dict3.setdefault('culoare', 'rosu')
print(x)
print(dict3)
# dict3.popitem()
# print(dict3)

dict4 = dict.fromkeys(dict3)
print(dict4)
x = {'key1', 'key2', 'key3'}
y = 1990
dict5 = dict.fromkeys(x, y)
print(dict5)

print(familie['copil1']['an'])
