#variabila = zona de memorie care tine date(diferite date)
#variabila = cutita cu valori
#ex2
tip_laptop = "HP"
model_laptop=  250
pret_laptop= 2350.99
stare_laptop_nou = True
#ex3
type(tip_laptop)
type(model_laptop)
type(pret_laptop)
type(stare_laptop_nou)
#ex4
pret_laptop=2350.99
round(2350.99)
print(round(2350.99))
#ex 5
print(f'Am cumparat un laptop {tip_laptop}')
print(f'Acesta este modelul {model_laptop}')
print(f'Pretul acestuia a fost de {pret_laptop} lei')
print(f'Starea acestuia fiind nou {stare_laptop_nou}')

#ex6
x=input('Nume')
y=input('Prenume')
z=len(x+y)
print(f'Numele complet are {z} caractere')

#ex 7
l=int(input('Lungime'))
k=int(input('Latime'))
a=int(k*l)

print(f'Aria dreptunghiului este {a}')

#ex8

my_str='Coral is either the stupidest animal or the smartest rock'
counting= my_str.count('the')
print(f'Cuvantul the este folosti de {counting} ori')

#ex9
replace = my_str.replace('the' ,'THE')
print(replace)

#ex10

verify = my_str.isdigit()
print(verify)

