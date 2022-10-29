word = input("Podaj wyraz: ")
word = list(word)

i=1
while i < len(word)-1:
    if word[i] == word[0]:
        word[i]="$"
    i+=1

word = "".join(word)
print(word)