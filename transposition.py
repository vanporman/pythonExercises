
import re

def transposition(text):

    text2 = re.sub('[^a-zA-Z]+', ' ', text)
    #print text2

    #l6hub stringi tyhiku kohapealt
    wordList = text2.split(' ')
    #print (wordList)

    for i in wordList:
        if i is '':
            indexOf = wordList.index(i)
            #print (indexOf)
            wordList.pop(indexOf)
    #print wordList
    longestWord = max(len(word) for word in wordList)
    output = []
    for i in range(longestWord):
        #for j in range(len(wordList)):
        output = ' '.join(word.ljust(longestWord)[i] for word in wordList)
        print (output)
        #    print '{:1}'.format(wordList[j][i]),
        #print
    #print (output)
    #return output


#transposition("Hello, World!")
transposition("Python CodeClub @ Tallinn")



##inf = float('inf')
###A = [[0,1,4,inf,3],
##     #[1,0,2,inf,4],
##     #[4,2,0,1,5],
##     #[inf,inf,1,0,3],
##     #[3,4,5,3,0]]
##A = ['Tere', 'homm']
##
###print('\n'.join([''.join(['{:4}'.format(item) for item in row])
###      for row in A]))
##def maatriks(n):
##
##    longestWord = max(len(word) for word in A)
##
##    print longestWord
##    print A
##    out = []
##    for i in range(longestWord):
##        for j in range(n):
##            out += A[j][i]
##            print '{:1}'.format(A[j][i]),
##        print
##    print out
##
##maatriks(len(A))
