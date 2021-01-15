import random as rnd 


def blanda_kort(kortlek):
    return rnd.shuffle(kortlek)

def kortlek_skapa():
    nummer = [i for i in range(2,11)]
    klädda = ['J', 'Q', 'K', 'A']

    nummer+=klädda
    kortlek= 4*nummer

    blanda_kort(kortlek)

    return kortlek
