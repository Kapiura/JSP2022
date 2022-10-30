from genericpath import sameopenfile


samogloski = ['a','e','y','i','o','ą','ę','u','ó']

literka = input("Wprowadz literke do sprawdzenia: ")

if literka in samogloski:
    print("To jest samogloska")
else:
    print("To jest spolgloska")
