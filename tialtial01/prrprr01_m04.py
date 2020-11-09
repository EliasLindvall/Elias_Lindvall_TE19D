'''
m04u01
'''
print("   m0401")
print("   ")

summa = 1

for i in range(1,11,2):
    summa = summa*i


print (summa)

print("   ")
print("   m04u02")
print("   ")

'''
m04u02
'''

konto = 10000
ff= 1.03

for i in range (15):
    
    konto = konto*ff
    print (f"efter {i+1} år finns det {konto} kr på kontot")
    print ("  ")


print("   ")
print("   m04u03")
print("   ")
'''
m04u03
'''
x = int(input("Vilken multiplikationstabell vill du skriva ut?"))
end = int(input("vart ska multiplikationstabellen sluta?"))
end = end+1

if x > 15:
      print("tabellen kan inte vara större än 15x15")
    
else: 
    for i in range (1,end):
        tabell= x*i
        print (tabell, end="  ")

print("   ")
print("   m04u04")
print("   ")
'''
m04u04
'''

tal=11

while tal > 1:
    tal -= 1
    print(tal, end=" ")


print("   ")
print("   m04u05")
print("   ")

'''
m04u05
'''

rats = 100
month = 0

while rats <1000000:
    rats = rats*2
    month += 1
    print (rats, end=" ")

print(f"det tar {month} månader tills det blir 1 miljon råttor i staden")
print("   ")
print("   m04e01")
print("   ")
'''
m04e01
'''
konto= 10000

år = 0

while år <15:
    år += 1
    konto = konto*1.03
    print(konto, end=" ")

print (f"det finns {konto}kr på kontot efter 15 år")

print("   ")
print("   m04e02")
print("   ")
'''
m04e02
'''

rats = 100
month = 0

for i in range(1000):
    rats = rats*2
    month +=1
    if rats >1000000:
        break

print (month)

print("   ")
print("   m04u06")
print("   ")
'''
m04u06
'''

tal = int(input("Vilket tal ska loopen börja med?"))

talend = int(input("Vilket tal ska loopen sluta på?"))

talskip = int(input("Vilket tal ska loopen inte skriva ut?"))

talbreak = int(input("Vilket tal ska avbryta loopen?"))

while tal < talend:
    tal += 1
    if tal == talskip:
        tal +=1
        print(tal)
    elif tal == talbreak:
        break
    else:
        print(tal)

print(f"loopen avbröts vid {talbreak}")

print("   ")
print("   m04u07")
print("   ")
'''
m04u07
'''
while True:
    try:
        tal = int(input("Vilket tal ska loopen börja med?"))
        break
    except:
        print("Du kan endast ange ett heltal, försök igen.")

while True:
    try:
        talend = int(input("Vilket tal ska loopen sluta på?"))
        break
    except:
        print("Du kan endast ange ett heltal, försök igen.")

while True:
    try:
        talskip = int(input("Vilket tal ska loopen inte skriva ut?"))
        break
    except:
        print("Du kan endast ange ett heltal, försök igen.")

while True:
    try:
        talbreak = int(input("Vilket tal ska avbryta loopen?"))
        break
    except:
        print("Du kan endast ange ett heltal, försök igen.")


while tal < talend:
    tal += 1
    if tal == talskip:
        tal +=1
        print(tal)
    elif tal == talbreak:
        break
    else:
        print(tal)

print(f"loopen avbröts vid {talbreak}")

print("   ")
print("   m04u08")
print("   ")
'''
m04u08
'''

tal = 5
lista = []

while tal != 0:
    tal = int(input("Skriv in ett heltal som ska vara i listan skriv ut 0 för att avsluta listan: "))
    if tal == 0:
        break
    lista.append(tal)
    

summa = (sum(lista))

maxvärde = (max(lista))

minvärde = (min(lista))

print(f"Summan av alla tal i listan är {summa}")
print(f"maxvärdet i listan är {maxvärde}")
print(f"minvärdet i listan är {minvärde}")

print("   ")
print("   m04u09")
print("   ")
'''
m04u09
'''

import random as rnd
slag = int(input("hur många tärningslag vill du göra? "))
dicelist = []

ettor = tvåor = treor = fyror = femmor = sexor = 0 

for n in range(slag):
    tal=rnd.randint(1,6)

    dicelist.append(tal)

    if tal == 1:
        ettor+=1
    elif tal ==2:
        tvåor+=1
    elif tal ==3:
        treor+=1
    elif tal ==4:
        fyror+=1
    elif tal ==5:
        femmor+=1
    elif tal ==6:
        sexor+=1

print(dicelist)

print(f"det finns {ettor} ettor, {tvåor} tvåor, {treor} treor, {fyror} fyror, {femmor} femmor och {sexor} sexor,")

