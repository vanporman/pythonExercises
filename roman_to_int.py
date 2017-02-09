
def roman_to_int(roman_general):
    myArr = list(roman_general)
    myNewArr = []
    print (myArr)
    for i in myArr:
        #print (i)
        if (i == 'I'):
            myNewArr.append(1)
        elif (i == 'V'):
            myNewArr.append(5)
        elif (i == 'X'):
            myNewArr.append(10)
        elif (i == 'L'):
            myNewArr.append(50)
        elif (i == 'C'):
            myNewArr.append(100)
        elif (i == 'D'):
            myNewArr.append(500)
        elif (i == 'M'):
            myNewArr.append(1000)

    print (myNewArr)

    #if (myNewArr.index(100)<myNewArr.index(1000)):

    #if (len(myNewArr) < 3 and myNewArr[0] < myNewArr[1]):
    #    romanNumb = myNewArr[1] - myNewArr[0]
    #else:
    romanNumb = sum(myNewArr)

    print (romanNumb)
    #return romanNumb

roman_to_int("MCMLIV")
roman_to_int("MCMXC")
roman_to_int("MMXIV")