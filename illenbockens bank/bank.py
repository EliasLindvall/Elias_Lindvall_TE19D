from functions import *

saldo = 1000

transaktioner = []

transaktioner.append(1000)

while True:

    meny = ("\n############################"
    "\n#                          #"
    "\n#    illenbockens bank     #"
    f"\n#       Saldo: {saldo} kr       #"
    "\n#                          #"
    "\n############################"
    "\n "
    "\n 1: Visa transaktioner."
    "\n 2: Sätt in pengar."
    "\n 3: Ta ut pengar."
    "\n 4: Avsluta applikationen.")

    print (meny)

    val = int(input("Vad vill du göra? (1-4): "))

    if val == 1:
        line=0
        summa=0
        head = ("\nAlla transaktioner"
        "\n {:>1} {:>11} {:>9}"
        "\n---------------------------").format("Nr", "Händelse", "Saldo")
        print(head)
        for i in transaktioner:
            line +=1
            summa +=i
            print("{:>2} {:>9} kr {:>9} kr".format(line,summa,saldo))


    elif val == 2:
        insättning = int(input("Hur mycket pengar vill du sätta in (kr)?"))
        if insättning > 0:
            saldo+=insättning
            transaktioner.append(insättning)
        else:
             print("insättningen kan inte vara negativ.")
    

    elif val == 3:
        uttag = int(input("Hur mycket pengar vill du ta ut (kr)?"))
        if uttag > saldo:
            print(f"Du kan inte ta ut mer än {saldo}")
        elif uttag < 0:
            print("uttaget kan inte vara negativt.")
        else:
            saldo-=uttag
            transaktioner.append(-uttag)

    elif val == 4:
        break



print(transaktioner)
