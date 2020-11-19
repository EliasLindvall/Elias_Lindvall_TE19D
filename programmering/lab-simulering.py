'''
Uppgift 1

a)
'''

print("   ")
print("   a)")
print("   ")

import math 

x2 = 0.5

y2 = 0.5

dist = math.sqrt((x2-0)**2 + (y2-0)**2)

print (f"distansen mellan punkterna är {dist}")

'''
# b)
'''
print("   ")
print("   b)")
print("   ")

import math 

x2 = 1

y2 = 1

dist = math.sqrt((x2-0)**2 + (y2-0)**2)

print (f"distansen mellan punkterna är {dist}")

'''
# c)
'''
print("   ")
print("   c)")
print("   ")
    
import math 

x2=0.5

y2=-0.5

dist = math.sqrt((x2-0)**2 + (y2-0)**2)

print (f"distansen mellan punkterna är {dist}")

'''
# d)
'''
print("   ")
print("   d)")
print("   ")

import math 
import random

x1= random.uniform(-1,1)

y1= random.uniform(-1,1)

x2= random.uniform(-1,1)

y2= random.uniform(-1,1)



print (x1, y1, x2, y2)

'''
# e)
'''
print("   ")
print("   e)")
print("   ")

import math
import random

summa = 0

punkter = 10000

for n in range (punkter):
    
    x1= random.uniform(-1,1)
    y1= random.uniform(-1,1)

    dist= math.sqrt((x1-0)**2 + (y1-0)**2)

    if dist <= 1:
        summa +=1


print(summa/punkter)


'''
f)
'''
'''
print("   ")
print("   f)")
print("   ")
import math 
import random


summa = 0

for i in range (10000):
    
    x1= random.uniform(-1,1)

    y1= random.uniform(-1,1)


    dist = math.sqrt((x1-0)**2 + (y1-0)**2)

    if dist <= 1:
        summa +=1
    

resultat = (summa * 4)/10000


print (f"resultatet blev {resultat}")
print (summa)

# desto mer punkter man simulerar desto närmare pi kommer resultatet.
# förhållandet mellan kvadratens area och cirkelns area är 4/pi därför blir cirkelns area gånger 4 delat på kvadratens area lika med pi.

'''
# g)
'''
print("   ")
print("   ")

import matplotlib.pyplot as plt
import math 
import random

summa = 0

for i in range (10000):
    
    x1= random.uniform(-1,1)

    y1= random.uniform(-1,1)


    dist = math.sqrt((x1-0)**2 + (y1-0)**2)

    if dist <= 1:
        plt.plot (x1, y1, 'g*')
    else:
        plt.plot (x1, y1, 'r*')


plt.show()
'''
'''
# h)
'''
print("   ")
print("   ")

import matplotlib.pyplot as plt
import math 
import random

summa = 0

for i in range (1000):
    
    x1= random.uniform(-2,2)

    y1= random.uniform(-2,2)


    dist = math.sqrt((x1-0)**2 + (y1-0)**2)

    if dist <= 1.5:
        plt.plot (x1, y1, 'g*')
    else:
        plt.plot (x1, y1, 'r*')


plt.show()
'''
Om man plottar t.ex 10 punkter åt gången så ser grafen väldigt rörig ut och det blir svårt att se vad den visar,
drar man upp det till 100 punkter blir det lite tydligare att se en liten cirkel i grafen. Testar man sedan 1000 punkter
blir det väldigt tydligt att se en cirkel i grafen som innehåller alla punkter med mindre avstånd än (i detta fallet 1.5) 1.5
och de som har större distans från origo än 1.5 utanför cirkeln.
'''