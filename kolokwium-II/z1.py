import numpy as np
import sys
import pathlib
currpath = str(pathlib.Path(__file__).parent.resolve())

if len(sys.argv) == 2:
    dane = sys.argv[1]
elif len(sys.argv) > 2:
    print("za dużo argumentów")
    sys.exit()
else:
    print("brak argumentu")
    sys.exit()
    
def palindrom(word):
    word = word.lower()
    word = list(word)
    word = np.array(word)
    word = word[::-1]
    word = np.delete(word, np.where(word == ' '))
    word = ''.join(word)
    if word == word[::-1]:
        return True
    else:
        return False


try:
    with open(dane, "r") as f:
        slowa = []
        for line in f:
            line = line[:len(line)-1]
            slowa.append(line)
except:
    print("nie można otworzyć pliku")
    sys.exit()
palindrom_path = currpath+'/palindromy.txt'
niepalindrom_path = currpath+'/nie_palindromy.txt'

with open(palindrom_path,'w') as pali:
    for i in slowa:
        if palindrom(i):
            pali.write(i+'\n')

with open(niepalindrom_path,'w') as niepali:
    for i in slowa:
        if not palindrom(i):
            niepali.write(i+'\n')
