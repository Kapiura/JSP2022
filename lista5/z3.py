rzym = {
    "M":1000,
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40,
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1,
    }
def rzymskie():
    liczba = 0
    x = input("Podaj liczbe rzymska: ")
    x = list(x)
    for dv, v in rzym.items():
        for i in range(len(x)):
            if x[i] == dv:
                liczba+=v
    return liczba
            
print("Ta liczba w systemie dziesiętnym to: ",rzymskie())