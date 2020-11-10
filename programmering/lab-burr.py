'''
Burr
a)
'''
'''
print("   ")
print("   a)")
print("   ")

for i in range(1,101):
    print(i)

print("   ")
print("   b)")
print("   ")
'''
# b)
'''

for i in range(1,101):
    if i%5 == 0:
        print("burr")
    else:
        print(i)

print("   ")
print("   c)")
print("   ")
'''
# c)
'''

burr = int(input("Skriv in vilket tal du vill ska bli Burr."))
birr = int(input("Skriv in vilket tal du vill ska bli Birr."))

BurrCounter = BirrCounter = 0

for i in range(1,101):
    if i%burr == 0:
        print("Burr")
    elif i%birr == 0:
        print("Birr")
    
    print(i)
'''
'''
# d)
'''

start = int(input("Vilket nummer ska spelet börja på? "))
end = int(input("Vilket nummer ska spelet sluta på? ")) + 1
burr = int(input("Skriv in vilket tal du vill ska bli Burr: "))
birr = int(input("Skriv in vilket tal du vill ska bli Birr: "))

BurrCounter = BirrCounter = 0

for i in range(start, end):
        
    if i%burr == 0:
        print("Burr")
        BurrCounter += 1
        
    if i%birr == 0:
        print("Birr")
        BirrCounter += 1
        
    
    
    print(i)



print(f"{BurrCounter} st Burr och {BirrCounter} st Birr")

'''
# f)
'''

start = int(input("Vilket nummer ska spelet börja på? "))
end = int(input("Vilket nummer ska spelet sluta på? ")) + 1
burr = int(input("Skriv in vilket tal du vill ska bli Burr: "))
birr = int(input("Skriv in vilket tal du vill ska bli Birr: "))

BurrCounter = BirrCounter = BurrBirrCounter = 0

for i in range(start, end):
    if i%burr == 0 and i%birr == 0:
        print(f"{i} = BurrBirr")
        BurrCounter +=1
        BirrCounter +=1
        BurrBirrCounter +=1
        
    elif i%burr == 0:
        print(f"{i} = Burr")
        BurrCounter += 1
        
    elif i%birr == 0:
        print(f"{i} = Birr")
        BirrCounter += 1
        
    else:
        print(i)

print(f"{BurrCounter} st Burr, {BirrCounter} st Birr och {BurrBirrCounter} st BurrBirr. ")

'''
Jag har lagt till en ny funktion i programmet, om Burr och Birr både är delbart med samma tal t.ex om vi väljer att Burr är 5 och Birr 10
så kommer programmet vid 10 istället för att både skriva ut Birr och Burr separat så kommer programmet skriva ut BurrBirr. Programmet räknar
Fortfarande BurrBirr som en  enskild Burr och Birr i Burr- och Birrcounter:n.
Istället för att ersätta talet med burr eller birr står det nu t.ex 5 = burr.
'''