'''
Uppgift 1

a)
'''

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

divsum = summa/3

print (f"procent av punkter som hamnade inom cirkeln {divsum*100}%")

'''
f)
'''
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



