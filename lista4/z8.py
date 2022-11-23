def szereg():
    n = int(input("Podaj liczbe n elementow "))
    suma = 0
    i=1
    while i <= n:
        suma+=(1/i)
        i+=1
    print(suma)
    
szereg()