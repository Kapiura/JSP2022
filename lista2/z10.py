lista = [i for i in range(0,100,3)]
print (lista)
del lista[4:len(lista):3]
print (lista)
print ("Suma:",sum(lista))
print ("Średnia:", sum(lista)/len(lista))