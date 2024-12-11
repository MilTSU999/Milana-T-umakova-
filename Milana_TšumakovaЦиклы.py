#Ül 3
p=0
for j in range(8):
    while True:
        try:
            arv=float(input("Sisesta {j+1} arv:"))
            break
        except:
            print("On vaja realne arv")
    if arv>0:
       p*=arv
    else:
        print("Korrutame arvud rohkem kui 0")
    print(f"{j+1}. samm korrutis= {p}")
print (f"Lõpptulemus on {p}")

#Ül 4
for i in range (10, 21,1):
    print(i**2, end=";")

#Ül 15
for rida in range(10):
    for veerg in range (10):
        print(veerg,end=" ")
    print()
print()

#Ül 16
for j in range(1, 10):
    for i in range(1,10):
        if i==j:
            print(j,end=" ")
        else:
            print ("0", end=" ")
    print()

#Ül 2
while True:
    try:
        A=int(input("Sisesta A:"))
        break
    except:
        print("On vaja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa+=i                #summa=summa+1
        print(f"i. samm summa={summa}")
    print(f"Vastus {summa}")
