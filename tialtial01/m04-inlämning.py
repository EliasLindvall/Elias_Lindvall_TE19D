
sid1 = int(input("Ange rektangelns första sida"))
sid2 = int(input("ange rektangelns andra sida"))

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



while True:
    sid1 = int(input("Ange rektangelns första sida"))
    sid2 = int(input("ange rektangelns andra sida"))

    area = sid1*sid2

    print(f"Rektangeln har sidorna {sid1} och {sid2} vilket gör arean till {area}")

    if sid1 == sid2:
        print("eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")


    for i in range(1,11):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

    while True:
        svar = str(input("Vill du göra en till beräkning ( j / n )?: "))
        if svar in ('j', 'n'):
            break
        print("felaktig input")
    if svar == 'y':
        continue
    else:
        break


    