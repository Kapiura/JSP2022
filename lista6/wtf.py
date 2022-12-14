lookansay = [[1]]
n = 4
i = 0
while i < n:
    poprzedni = lookansay[i]
    tymczasowa = []
    dl = len(poprzedni)
    v = 1
    k = 0



    while k < dl:
        if k+1 < dl-1:
            print('test')
            if poprzedni[k] == poprzedni[k+1]:
                v+=1
            tymczasowa.append(v)
            tymczasowa.append(poprzedni[k])
            k+=1
        k+=1
    
    i+=1
    lookansay.insert(i,tymczasowa)





for m in range(len(lookansay)-1):
    print(lookansay[m])