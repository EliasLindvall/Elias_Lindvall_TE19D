from functions import *
import os
move_transactions()
    
# Programloopen
while True:
    # Skriver ut menyn och frågar användar efter sitt val
    meny = ("\n############################"
    "\n#                          #"
    "\n#    illenbockens bank     #"
    f"\n#       Saldo: {balance()}kr      #"
    "\n#                          #"
    "\n############################"
    "\n "

    "\n 1: Visa transaktioner."
    "\n 2: Sätt in pengar."
    "\n 3: Ta ut pengar."
    "\n 4: Nollställ kontot"
    "\n 5: Avsluta applikationen."
    "\n Gör ditt val (1-5):")

    print meny

    val = validate_int(meny, "Felaktig inmatning! Gör om gör rätt.")

    if val == 1:
        print_transactions()


    elif val == 2:
        insättning = validate_int("Hur mycket pengar vill du sätta in (kr)?","Felaktig inmatning! Gör om gör rätt.")
        if insättning > 0:
            add_transaction(insättning, True)
        else:
             print("insättningen kan inte vara negativ.")
    

    elif val == 3:
        uttag = validate_int("Hur mycket pengar vill du ta ut (kr)?", "Felaktig inmatning! Gör om gör rätt.")
        if uttag > balance():
            print(f"Du kan inte ta ut mer än {balance()}")
        elif uttag < 0:
            print("uttaget kan inte vara negativt.")
        else:
            add_transaction(-uttag, True)  

    elif val == 4:
        nollställ= int(input("Är du säker detta nollställer hela kontot?\n1. Ja\n2. Nej"))
        if nollställ == 1:
            os.remove(filename)
            transaktioner.clear()
            move_transactions()
        else:
            continue

    elif val == 5:
        break


