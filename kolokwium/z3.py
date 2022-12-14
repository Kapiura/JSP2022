import math
#program działa tylko dla m, cm i mm
def zamiana(r, jednostka):
    if jednostka == 'm':
        r = r
        pole  = math.pi*(r**2)
        return pole
    elif jednostka == 'cm':
        r = r/100
        pole  = math.pi*(r**2)
        return pole
    elif jednostka == 'mm':
        r = r/1000
        pole  = math.pi*(r**2)
        return pole
    else:
        print("Błędnie podane jednostki, masz do wyboru tlyko cm, m oraz mm!")

r = int(input("Podaj promień koła: "))
jed = input("W jakich jednostkach podałes dany promień: ")
if zamiana(r,jed) != None:
    print("Pole koła wynosi: ",zamiana(r,jed),"m^2")