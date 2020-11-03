'''
m04u01
'''
print("   m0401")
print("   ")

summa = 1

for i in range(1,11,2):
    summa = summa*i


print (summa)

print("   ")
print("   m04u02")
print("   ")

'''
m04u02
'''

konto = 10000
ff= 1.03

for i in range (15):
    
    konto = konto*ff
    print (f"efter {i+1} år finns det {konto} kr på kontot")
    print ("  ")


print("   ")
print("   m04u03")
print("   ")
'''
m04u03
'''
x = int(input("Vilken multiplikationstabell vill du skriva ut?"))
end = int(input("vart ska multiplikationstabellen sluta?"))
end = end+1

if x > 15:
      print("tabellen kan inte vara större än 15x15")
    
else: 
    for i in range (1,end):
        tabell= x*i
        print (tabell, end="  ")

print("   ")
print("   m04u04")
print("   ")
'''
m04u04
'''

tal=11

while tal >1:
    tal -=1
    print(tal, end=" ")


print("   ")
print("   m04u05")
print("   ")
'''
m04u05
'''

rats = 100
month =0

while rats <1000000:
    rats *2
    month += 1

print(f"det tar {month} månader tills det blir 1 miljon råttor i staden")
