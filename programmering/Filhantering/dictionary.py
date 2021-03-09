person = dict(
    namn = 'Elias',
    ålder = 17,
    yrke = 'pluggar',
    arbetsplats = 'NTI' 
)

print (person)
print (F"Personens namn är {person['namn']}")
print (f"Han är {person['ålder']} år gammal")


overwatch = {
    "Pharah":"Guldvapen",
    "Mcree":"Guldvapen",
    "Reinhart":"Ej Guldvapen"
}



for key, value in overwatch.items():
    print (f"{key}     \t{value}")
    