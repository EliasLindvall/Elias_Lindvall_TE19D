'''
Uppgift 1

a)
'''
print("   ")
print("   a)")
print("   ")
import math 

x1=0

y1=0

x2=0.5

y2=0.5

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print (f"distansen mellan punkterna är {dist}")

'''
b)
'''
print("   ")
print("   b)")
print("   ")

import math 

x1=0

y1=0

x2=1

y2=1

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print (f"distansen mellan punkterna är {dist}")

'''
c)
'''
print("   ")
print("   c)")
print("   ")
    
import math 

x1=0

y1=0

x2=0.5

y2=-0.5

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print (f"distansen mellan punkterna är {dist}")

'''
d)
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
e)
'''
print("   ")
print("   e)")
print("   ")

import math
import random

summa=0

for n in range (20):
    
    x1= random.uniform(-1,1)
    y1= random.uniform(-1,1)

    dist= math.sqrt((x1-0)**2 + (y1-0)**2)

    if dist <= 1:
        summa +=1


print(summa)


'''
f)
'''
print("   ")
print("   ")
import math 
import random

summa=0

x1= 0

y1= 0

x2= random.uniform(-1,1)

y2= random.uniform(-1,1)

x3 = random.uniform(-1,1)

y3 = random.uniform(-1,1)

x4 = random.uniform(-1,1)

y4 = random.uniform(-1,1)

dist1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)

dist2 = math.sqrt((x4-x1)**2 + (y3-y1)**2)

dist3 = math.sqrt((x4-x1)**2 + (y4-y1)**2)

if dist1 < 1:
    summa += 1

if dist2 < 1:
    summa += 1

if dist3 < 1:
    summa += 1

multsum = summa*4

print (multsum)


'''
g)
'''
print("   ")
print("   ")

import matplotlib as plt
import math 
import random

summa=0

x1= 0

y1= 0

x2= random.uniform(-1,1)

y2= random.uniform(-1,1)

x3 = random.uniform(-1,1)

y3 = random.uniform(-1,1)

x4 = random.uniform(-1,1)

y4 = random.uniform(-1,1)

x5 = random.uniform(-1,1)

y5 = random.uniform(-1,1)

dist1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)

dist2 = math.sqrt((x4-x1)**2 + (y3-y1)**2)

dist3 = math.sqrt((x4-x1)**2 + (y4-y1)**2)

dist4 = math.sqrt((x5-x1)**2 + (y5-y1)**2)

if dist1 < 1:
    summa += 1

if dist2 < 1:
    summa += 1

if dist3 < 1:
    summa += 1

if dist4 < 1:
    summa += 1

plt.plot (x2, y2, '*r')
plt.plot (x3, y3, '*g')
plt.show
print (summa)



