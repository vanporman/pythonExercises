
def charswap(name):

    if (name is not str):
        name2 = str(name)
        myArr = list(name2)
    elif (name == ''):
        myArr = []
    else:
        myArr = list(name)
    #print (name)
    #print myArr
    #print (len(myArr))
    if (len(myArr) == 0):
        output = ''
    else:
        firstChar = myArr[0]
        lastChar = myArr[len(myArr)-1]
        myArr[0] = lastChar
        myArr[len(myArr)-1] = firstChar
        output = ''.join(str(i) for i in myArr)
    #print (output)
    #print(len(output))
    return output

charswap("Jaagup")
charswap(100)
charswap(" i a u")
charswap("s")
charswap(1)
charswap('')


