
import re

def transposition(text):

    text2 = re.sub("[^a-zA-Z' '0-9]+", "", text)
    #print text2

    #l6hub stringi tyhiku kohapealt
    wordList = text2.split(' ')
    #print (wordList)

    for i in wordList:
        if i is '': #<--- seda muuta, et v6taks tyhja v6i miks teeb @ m2rgist tyhja
            indexOf = wordList.index(i)
            #print (indexOf)
            wordList.pop(indexOf)
    #print wordList
    longest = max(len(word) for word in wordList)
    for i in range(longest):
        output = ' '.join(word.ljust(longest)[i] for word in wordList)
        print (output)
        #return ' '.join(word.ljust(longest)[i] for word in wordList)

transposition("Hello, World!")
#transposition("Pyhton CodeClub @ Tallinn")

