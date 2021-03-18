'''
person = dict(
    namn = 'Elias',
    ålder = 17,
    yrke = 'pluggar',
    arbetsplats = 'NTI' 
)

print (person)
print (F"Personens namn är {person['namn']}")
print (f"Han är {person['ålder']} år gammal")


Guldvapen? = {
    "Pharah":"True",
    "Mcree":"True",
    "Reinhart":"False"
}



for key, value in overwatch.items():
    print (f"{key}     \t{value}")

'''
'''
# uppgift 1

kurser = {
    "prog1":100,
    "web1":50,
    "ma3":100,
    "sve2":100,
    "fy1":100,
    "tial1":50,
    "idr1":100,
    "eng6":100,
    "daodac1":100
}

print (f"Jag läser just nu {sum(kurser.values())} poäng.")

'''
'''
import random as rnd
#uppgift 2

ettor = tvåor = treor = fyror = femmor = sexor = 0

for i in range(100000):
    x = rnd.randint(1,6)

    if x == 1:
        ettor +=1
    elif x == 2:
        tvåor +=1
    elif x == 3:
        treor +=1
    elif x == 4:
        fyror +=1
    elif x == 5:
        femmor +=1
    else:
        sexor +=1

Frekvenstabell = {
    "1":ettor,
    "2":tvåor,
    "3":treor,
    "4":fyror,
    "5":femmor,
    "6":sexor
}
print ("Frekvenstabell")
for key, value in Frekvenstabell.items():
    print (f"{key}:  {value}")

'''

#uppgift 3
