'''
sid1 = int(input("Ange rektangelns första sida: "))
sid2 = int(input("ange rektangelns andra sida: "))

area = sid1*sid2

print(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")

if sid1 == sid2:
    print("eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")


for i in range(1,11):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

print(" ")
print("b")
print(" ")
'''

'''

rekinfo = []

while True:
    sid1 = int(input("Ange rektangelns första sida: "))
    sid2 = int(input("ange rektangelns andra sida: "))

    area = sid1*sid2

    print(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")

    if sid1 == sid2:
        print("eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")

    if sid1 == sid2:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}, eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")
    else:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")
        


    for i in range(1,11):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

    while True:
        svar = str(input("Vill du göra en till beräkning ( j / n )?: "))
        if svar in ('j', 'n'):
            break
        print("felaktig input")
    if svar == 'j':
        continue
    else:
        break


print(*rekinfo, sep = "\n")


'''

'''
'''
'''
rekinfo = []

while True:
    sid1 = int(input("Ange rektangelns första sida: "))
    sid2 = int(input("ange rektangelns andra sida: "))

    while True:
        try:
            höjd = int(input("ange rätblockets höjd: "))
            break
        except:
            print("Du har gjort en felaktig inmatning, ange ett heltal")
            
    
    if höjd <1:
        höjd = 1
        print("Eftersom du matade in ett negativt tal så sattes höjden automatiskt till 1")
    if höjd >10:
        höjd=10
        print("Eftersom du matade in ett tal som var större än 10 så sänktes höjden automatiskt till 10")

    area = sid1*sid2

    print(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")

    if sid1 == sid2:
        print("eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")

    if sid1 == sid2:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}, eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")
    else:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")
        


    for i in range(1,höjd+1):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

    while True:
        svar = str(input("Vill du göra en till beräkning ( j / n )?: "))
        if svar in ('j', 'n'):
            break
        print("felaktig input")
    if svar == 'j':
        continue
    else:
        break


print(*rekinfo, sep = "\n")
'''
'''
d
'''
rekinfo = []

sidor = []
höjder = []
while True:
    sid1 = int(input("Ange rektangelns första sida: "))
    sid2 = int(input("ange rektangelns andra sida: "))

    while True:
        try:
            höjd = int(input("ange rätblockets höjd: "))
            break
        except:
            print("Du har gjort en felaktig inmatning, ange ett heltal")
            
    if höjd <1:
        höjd = 1
        print("Eftersom du matade in ett negativt tal så sattes höjden automatiskt till 1")
    if höjd >10:
        höjd=10
        print("Eftersom du matade in ett tal som var större än 10 så sänktes höjden automatiskt till 10")

    sidor.append(sid1)
    sidor.append(sid2)
    höjder.append(höjd)
    area = sid1*sid2

    print(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")

    if sid1 == sid2:
        print("eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")

    if sid1 == sid2:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}, eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")
    else:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")
        


    for i in range(1,höjd+1):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

    while True:
        svar = str(input("Vill du göra en till beräkning ( j / n )?: "))
        if svar in ('j', 'n'):
            break
        print("felaktig input")
    if svar == 'j':
        continue
    else:
        break

print(*rekinfo, sep = "\n")

print(sidor)
print(höjder)

'''
e
'''

def räkna_area(sid1, sid2):
    return sid1*sid2

rekinfo = []

while True:
    sid1 = int(input("Ange rektangelns första sida: "))
    sid2 = int(input("ange rektangelns andra sida: "))

    while True:
        try:
            höjd = int(input("ange rätblockets höjd: "))
            break
        except:
            print("Du har gjort en felaktig inmatning, ange ett heltal")
            
    
    if höjd <1:
        höjd = 1
        print("Eftersom du matade in ett negativt tal så sattes höjden automatiskt till 1")
    if höjd >10:
        höjd=10
        print("Eftersom du matade in ett tal som var större än 10 så sänktes höjden automatiskt till 10")

    area = räkna_area(sid1,sid2)

    print(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")

    if sid1 == sid2:
        print("eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")

    if sid1 == sid2:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}, eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")
    else:
        rekinfo.append(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")
        


    for i in range(1,höjd+1):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

    while True:
        svar = str(input("Vill du göra en till beräkning ( j / n )?: "))
        if svar in ('j', 'n'):
            break
        print("felaktig input")
    if svar == 'j':
        continue
    else:
        break