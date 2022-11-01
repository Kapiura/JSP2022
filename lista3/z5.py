import re

pas = input("Wprowadz hasło: ")

x = re.search("[$#@]",pas)
y = re.search("[a-zA-Z]",pas)
z = re.search("[0-9]",pas)
if x != None and z != None and y != None and len(pas)>=6 and len(pas)<=16:
    print("Gratuluje, hasło spełnia wymagania")
else:
    print("Hasło nie spełnia wymagań")