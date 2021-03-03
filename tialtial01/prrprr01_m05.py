'''
def jag():
    print('Elias Te19D NTI Kronhus')

jag()

'''

'''
'''
import math
def area_cirkel(radie):
    return math.pi*radie**2

def omkrets_cirkel(radie):
    return 2*radie*math.pi

r = int(input("Ange radien till en cirkel: "))

a = area_cirkel(r)

o = omkrets_cirkel(r)

print(f"cirkelns omkrets är {o} och cirkelns area är {a}")



