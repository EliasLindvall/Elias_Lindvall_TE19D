from config import *
import os

def balance():
    balance=0
    for t in transaktioner:
        balance+=t
    return balance

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def print_transactions():
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

def check_file_exists():

    try:
        with open(filename, "x"):
            print (f"filen {filename} skapades")
        
        with open(filename, "a") as f:
            f.write(f"1000\n")
    except:
        return


def move_transactions():

    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                transaktioner.append(int(rad))

def add_transaction(transaktion, toFile = False):
    transaktioner.append(transaktion)
    if toFile:
        write_transaction_to_file(transaktion)

def write_transaction_to_file(transaktion):
    with open(filename, "a") as f:
        f.write(f"{transaktion}\n")