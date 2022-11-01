from itertools import chain
los= [i for i in range(100,401,1)]
wynik = []

i=0


while i < len(los):
    mor = [int(x) for x in str(los[i])]
    if mor[0]%2==0 and mor[1]%2==0 and mor[2]%2==0:
        wynik.append(los[i])
    i+=1
print(wynik)