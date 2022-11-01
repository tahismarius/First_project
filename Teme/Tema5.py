#ex b.1
def suma_a_2numer(nr1 , nr2):
        return int(nr1)+ int(nr2)

suma=suma_a_2numer(1 ,2)
print(suma)

suma_2=suma_a_2numer(687 , 542 )
print(suma_2)

ex b.2
def Par_Impar(numar):
    if numar%2 == 0:
        return True
    else:
        return False


numar = Par_Impar(2)
print(f'Numarul este Par : {numar}')

numar = Par_Impar(11)
print(f'Numarul este Par : {numar}')

ex b.3

def Nume(nume , prenume , nume_mijlociu):
    return len(nume)+ len(prenume) + len(nume_mijlociu)

n=Nume('Tahis','Marius','Alexandru')
print(n)

m=Nume('Ion','Anton','Vasile')
print(m)

ex b.4
def Aria_Dreptunghiului(lungime,latime):
    a=int(lungime)*int(latime)
    return f'Aria dreptunghiului este {a} '


f=Aria_Dreptunghiului(2,5)
print(f)

g=Aria_Dreptunghiului(10,12)
print(g)

ex b.5
def Aria_cercului(raza,pi=3.14):
    a=raza*pi
    return f'Aria cercului este {a}'

h=Aria_cercului(13.4)
print(h)

j=Aria_cercului(45)
print(j)

ex b.6

def caracter(n,m):
    if m in n:
        return True
    else:
        return False


x=caracter('Maria are mere', 'Maria')
print(x)

y=caracter('Ion invata python', 'Html')
print(y)


ex b.7
def functie():
    a=input('Introduceti string:')
    count1=0
    count2=0
    for i in a:
        if(i.islower()):
            count1= count1+1
        elif(i.isupper()):
            count2 = count2+1
    print(f'Nr de caractere lower case este {count1}')
    print(f'Nr de caractere upper este {count2}')

print(functie())

#ex b.8
def lista_pozitive(l):
    lista_gola=[]
    for x in l:
        if x >= 0:
            lista_gola.append(x)
    return lista_gola

c=lista_pozitive([1,2,3,4,5,-1,-3,-5])
print(c)

#ex b.9
def numere(a,b):
    if a>b:
        print(f'Primul numar {a} este mai mare dacat al doilea nr {b}')
    elif a<b:
        print(f'Al doilea numar {b} este mai mare decat primul {a}')
    else:
        print(f'Numerele sunt egale')

s=numere(1,1)
print(s)

d=numere(1,2)
print(d)

f=numere(2,1)
print(f)

ex b.10

def functie(a,b):
    if a not in b:
        print(f'am adaugat numarul in noul set')
        return True
    elif a in b:
        print(f'Nu am adaugat numarul in set. Acesta exista deja')
        return False


a=functie('1', '1,2,3,4,5,6,7,8')
print(a)

b=functie('0','1,2,3,4,5,6,7')
print(b)

ex c.11


a=None
def zile_luna(a):
    if a== 'Ianuarie':
       return '31 de zile'
    elif a== 'Februarie':
        return '28 de zile '
    elif a== 'Martie':
       return '31 de zile'
    elif a== 'Aprilie':
        return '30 de zile '
    elif a== 'Mai':
       return '31 de zile'
    elif a== 'Iunie':
        return '30 de zile '
    elif a== 'Iulie':
       return '31 de zile'
    elif a== 'August':
        return '31 de zile '
    elif a== 'Septrmbrie':
       return '30 de zile'
    elif a== 'Octombrie':
        return '31 de zile '
    elif a== 'Noiembrie':
       return '30 de zile'
    elif a== 'Decembrie':
        return '31 de zile '
b=zile_luna('Februarie')
print(b)

c=zile_luna('Noiembrie')
print(c)






