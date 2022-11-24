def zamiana(liczba):
    liczbowo = {
        1: 'jeden',
        2: 'dwa',
        3: 'trzy',
        4: 'cztery',
        5: 'pięć',
        6: 'sześć',
        7: 'siedem',
        8: 'osiem',
        9: 'dziewięć',
        10: 'dziesięć',
        11: 'jedenaście',
        12: 'dwanaście',
        13: 'trzynaście',
        14: 'czternaście',
        15: 'piętnaście',
        16: 'szesnaście',
        17: 'siedemnaście',
        18: 'osiemnaście',
        19: 'dziewiętnaście',
        20: 'dwadzieścia',
        30: 'trzydzieści',
        40: 'czterdzieści',
        50: 'pięćdziesiąt',
        60: 'sześćdziesiąt',
        70: 'siedemdziesiąt',
        80: 'osiemdziesiąt',
        90: 'dziewięćdziesiąt',
        100: 'sto',
        200: 'dwieście',
        300: 'trzysta',
        400: 'czterysta',
        500: 'pięćset',
        600: 'sześćset',
        700: 'siedemset',
        800: 'osiemset',
        900: 'dziewięćset',
        1000: 'tysiąc'
    }
    slownie = []
    liczba = str(liczba)
    listaliczba= list(liczba)
    trulista = []
    for i in range(len(listaliczba)):
        w = int(listaliczba[i])
        trulista.append(w) 
    l = len(trulista)
    for i in range(len(trulista)):
        w = 10**(l-1)
        trulista[i] *=w
        l-=1
    for dv, v in liczbowo.items():
        for i in range(len(trulista)):
            if dv == trulista[i]:
                slownie.append(v)
    slownie.reverse()
    slowo = ' '.join(slownie)
    return slowo
                

liczba = int(input("Podaj liczbę od 1 do 1999: "))
print(zamiana(liczba))