from socket import J1939_EE_INFO_NONE


s = ["Kasia", "Basia", "Marek", "Darek"]
print (1,s)

s.append("Józek")
print (2,s)

s.extend(["Ania","Basia"])
print (3,s)

s.sort()
print (4,s)

print (5,s[3])

print (6,s[0:2])

ls = len(s)
print (7,s[ls-2:])

i=ls-1
czy = 0
while i >= 0:
    if czy !=0 and s[i]=="Basia":
        s.remove(s[i])
    if s[i] == "Basia":
        czy = 1
    i-=1


print (8,s)

print (9,len(s))
 
s=tuple(s)
print(10,s)