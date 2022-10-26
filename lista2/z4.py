word = input("Podaj napis: ")

for i in range(len(word)-1):
    i+=1
    if word[i] == word[0]:
        word.replace(word[i],"s")

print (word)