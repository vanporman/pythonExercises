
def is_person_code_valid(idcode):

    #kontrollib, kas on string, kui ei ole, siis muudab stringiks ja lisa listi
    if (idcode is not str):
        strIdCode = str(idcode)
        idArr = list(strIdCode)
    #lisab otse listi
    else:
        idArr = list(idcode)
    #print (idArr)

    #muudab listi elemendid int-ideks
    idArr = [int(i) for i in idArr]
    print (idArr)

    #arvitab lsiti numbrite summa
    sumOfIdArr = 0
    for i in idArr:
        sumOfIdArr += i
    #print (sumOfIdArr)

    firstgrade = [1,2,3,4,5,6,7,8,9,1]
    #print (firstgrade)
    secondgrade = [3,4,5,6,7,8,9,1,2,3]

    firstgradeweighsum = [a*b for a,b in zip(idArr,firstgrade)]
    #print (firstgradeweighsum)
    sumoffirstgradeweigh = int(sum(firstgradeweighsum))
    print (sumoffirstgradeweigh)

    firstgradeweighmodulo = int(sumoffirstgradeweigh/11)
    print (firstgradeweighmodulo)
    calc1 = int(firstgradeweighmodulo*11)
    print (calc1)
    controlnumber1 = int(sumoffirstgradeweigh - calc1)
    #print ("last number of idcode: ", controlnumber1)

    if (controlnumber1 == 10):
        secondgradeweighsum = [a*b for a,b in zip(idArr, secondgrade)]
        #print ("SGW: ", secondgradeweighsum)
        sumofsecondgradeweigh = int(sum(secondgradeweighsum))
        #print ("SGW: ", sumofsecondgradeweigh)

        secondgradeweighmodulo = int(sumofsecondgradeweigh/11)
        #print ("SGW: ", secondgradeweighmodulo)
        calc2 = int(secondgradeweighmodulo*11)
        #print ("SGW: ", calc2)
        controlnumber2 = int(sumofsecondgradeweigh - calc2)
        #print("SGW: ", controlnumber2)

        if (controlnumber2 == 10):
            controlnumber3 = 0
            print ("2 last number of idcode: ", controlnumber3)
            return True
        elif (controlnumber2 != idArr[10]):
            print ("2 this is not id code", controlnumber2)
            return False
        else:
            print ("2 last number of idcode: ", controlnumber2)
            return True
    elif (controlnumber1 != idArr[10]):
        print ("1 this is not id code", controlnumber1)
        return False
    else:
        print ("1 last number of idcode: ", controlnumber1)
        return True

is_person_code_valid("49403136526")
