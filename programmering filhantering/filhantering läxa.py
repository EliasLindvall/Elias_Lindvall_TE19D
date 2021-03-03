# uppgift 1
# a)
import random as rnd

def diceroll():
     return rnd.randint(1,6)
    
rolls = []

for i in range(10):
    rolls.append(diceroll())

with open("diceRoll.txt", "w") as ok:
    for number in rolls:
        ok.write(str(number))

