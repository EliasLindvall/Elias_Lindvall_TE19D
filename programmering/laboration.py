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
