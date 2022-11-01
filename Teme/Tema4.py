#Ex.1)
masini = ["Audi","Volvo","Mercedes","Aston Martin","Lastun","Fiat","Trabant","Opel"]
# for x in range(0,len(masini)):
#a)
#     print(f"Masina mea preferata este {masini[x]}")
# #b)
# for x in masini:
#     print((f"Masina mea preferata este {x}"))
# #c)
# x = 0
# while (x < len(masini)):
#     print(f"Masina mea preferata este {masini[x]}")
#     x += 1

#Ex.2)
# for x in range(1,len(masini)-1):
#     masini[x] = masini[x].upper()
# else:
#     print(masini)

#Ex.3)
# for x in masini:
#     if x == "Mercedes":
#         print(f"Am gasit masina {x} dorita de dumneavoastra!")
#         break
#     else:
#         print(f"Am gasit masina {x}.Mai cautam.")

# Ex.4)
# for x in masini:
#     if x=="Trabant":
#         continue
#     if x=="Lastun":
#         continue
#     else:
#         print(f"S-ar putea sa va placa masina {x}")

# Ex.5)
# masini_vechi=[]
# for x in range(len(masini)):
#     if masini[x]=="Lastun":
#         masini_vechi.append("Lastun")
#         masini[x]="Tesla"
#     if masini[x]=="Trabant":
#         masini_vechi.append("Trabant")
#         masini[x]="Tesla"
# print(f"Modelele noi sunt {masini}")
# print((f"Modelele vechi sunt {masini_vechi}"))

# Ex.6)
# pret_masini={
#     "Dacia":6800,
#     "Lastun":500,
#     "Opel":1100,
#     "Audi":19000,
#     "BMW":23000
#     }
# buget=15000
# for key,value in pret_masini.items():
#     if value<= buget:
#         print(f"Pentru un buget de {buget} euro puteti alege masina {key}!")

# Ex.7)
# numere=numere=[5,7,3,9,3,3,1,0,-4,3]
# apare3 = []
# for x in numere:
#     if x==3:#daca gaseste 3
#          apare3.append(x)
# print(f"Numarul 3 apare de {len(apare3)}")

# Ex.8
# a=0
# for numar in numere:
#    #calculam elementele pas cu pas
#     a=a+numar
# print(f"Suma este {a}")

# Ex.9)
# for x in numere:
#     x= sorted(numere)[5]
# print(x)

#Ex.10)
# for x in range(0,len(numere)):
#     if x>=0:
#         numere[x]=-numere[x]
# print(numere)

#Ex.11)
alte_numere = [-5,7,2,9,12,3,1,-6,-4,3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for x in alte_numere:
    if x >= 0 :
        numere_pozitive.append(x)
    if x < 0:
            numere_negative.append(x)
    if x % 2 == 0 and x>0:
        numere_pare.append(x)
    else:
        numere_impare.append(x)
print(numere_negative)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)