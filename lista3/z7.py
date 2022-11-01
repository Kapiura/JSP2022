from cmath import pi


N =  int(input("Podaj N: "))

i=0

pier = 0
drugi = 1
trzeci = drugi+ pier

while i < N:
    i+=1
    print(trzeci,end=", ")
    trzeci = drugi+ pier
    pier=drugi
    drugi = trzeci
