def zamiana(sl):
    slownie = {
        'jeden' : 1,
        'dwa' : 2,
        'trzy' : 3,
        'cztery' : 4,
        'pięć' : 5,
        'sześć' : 6,
        'siedem' : 7,
        'osiem' : 8,
        'dziewięć' : 9,
        'dziesięć' : 10,
        'jedenaście' : 11,
        'dwanaście' : 12,
        'trzynaście' : 13,
        'czternaście' : 14,
        'piętnaście' : 15,
        'szesnaście' : 16,
        'siedemnaście' : 17,
        'osiemnaście' : 18,
        'dziewiętnaście' : 19,
        'dwadzieścia' : 20,
        'trzydzieści' : 30,
        'czterdzieści' : 40,
        'pięćdziesiąt' : 50,
    }
    slista = sl.split()
    liczba = 0
    for dv, v in slownie.items():
        for i in range(len(slista)):
            if dv == slista[i]:
                liczba+=v
    return liczba

slowo = input("Podaj liczbe słownie od 1 do 59: ")
print(zamiana(slowo))