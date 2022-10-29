from socket import J1939_EE_INFO_NONE


s = ["Kasia", "Basia", "Marek", "Darek"]
print (s)

s.append("Józek")
print (s)

s.extend(["Ania","Basia"])
print (s)

s.sort()
print (s)

print (s[3])

print (s[0:2])

ls = len(s)
print (s[ls-2:])

i=ls-1
while i >= 0:
    if s[i] == "Basia":
        s.pop(i)
    i-=1


print (s)

print (len(s))
 
s=tuple(s)
print(s)