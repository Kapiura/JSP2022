A = [[1,2],{'jeden': '1', 'dwa':'2'}]
print(A)
jedynki = ['1'] * 97
jedynki = "".join(jedynki)
jedynki = int(jedynki)
A[1]["jeden"] = jedynki
print(A)