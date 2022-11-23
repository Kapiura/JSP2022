def silnia():
    n = int(input("Podaj liczbe n : "))
    i = 1 
    iloczyn = 1
    if n < 0 :
        print("n musi nalezec do liczb naturalnych dodatnich")
    else:
        while i <= n:
            iloczyn*=i
            i+=1
        print (iloczyn)

silnia()