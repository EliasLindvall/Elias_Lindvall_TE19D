from config import *

def balance():      # Beräknar saldot
    balance=0
    for t in transaktioner:
        balance+=t
    return balance

def validate_int(output, error_mess):       # Kollar om inputen är ett heltal
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def print_transactions():       # skriver ut transaktionslistan
        line=0
        summa=0
        head = ("\n    Alla transaktioner\n"
            "\n {:>1} {:>11} {:>10}"
            "\n---------------------------").format("Nr", "Händelse", "Saldo")
        print(head)
        for i in transaktioner:
            line +=1
            summa += i
            print("{:>2} {:>9} kr {:>9} kr".format(line,i,summa))

def check_file_exists():        # Kollar om "transaktioner.txt" finns om inte så skapas den
    try:
        with open(filename, "x"):
            print (f"filen {filename} skapades")
        
        with open(filename, "a") as f:
            f.write(f"1000\n")
    except:
        return


def move_transactions():        # Lägger till alla transaktioner från "transaktioner.txt" till listan transaktioner

    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                transaktioner.append(int(rad))

def add_transaction(transaktion, toFile = False):       # Lägger till en transkation till listan och filen "transaktioner.txt"
    transaktioner.append(transaktion)
    if toFile:
        write_transaction_to_file(transaktion)

def write_transaction_to_file(transaktion):     # Skriver en transaktion till filen "transaktioner.txt"
    with open(filename, "a") as f:
        f.write(f"{transaktion}\n")