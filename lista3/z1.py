import re
samogloski = ['a','e','y','i','o','ą','ę','u','ó','A','E','Y','I','O','Ą','Ę','U','Ó']

literka = input("Wprowadz literke do sprawdzenia: ")
y = re.search("[a-zA-Z]",literka)
if y is None:
    print("to nie jest literka")
else:
    if literka in samogloski:
        print("To jest samogloska")
    else:
        print("To jest spolgloska")

