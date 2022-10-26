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
for i in s:
    if i == "Basia":
        s.remove("Basia")
        s.remove("Basia")
print (s)

print (len(s))
 
s=tuple(s)
print(s)