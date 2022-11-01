
#ex16
import math
string_impar =input('Introduceti un string impar')
x=string_impar[math.floor(len(string_impar)/2)]
print(x)

#ex19
var='alabala portocala'
lista = var.split()
print(lista)
primul=var[0]
print(primul)
litera_mare=var[1:-1].replace('a' , 'A')
print(primul + litera_mare + primul)

#ex 20
x=input('User')
y=input('Parola')
y_len=(len(y))
obf = str(y_len * '*')
print(f'Userul este {x},\n parola lui este {obf}, \n si are {y_len} caractere')


