
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
    #sumOfIdArr = 0
    #for i in idArr:
    #    sumOfIdArr += i
    #print (sumOfIdArr)

    #IjaII astme kaalud
    firstgrade = [1,2,3,4,5,6,7,8,9,1]
    secondgrade = [3,4,5,6,7,8,9,1,2,3]

    firstgradeweighsum = [a*b for a,b in zip(idArr,firstgrade)]
    print (firstgradeweighsum)
    sumoffirstgradeweigh = int(sum(firstgradeweighsum))
    print (sumoffirstgradeweigh)

    firstgradeweighmodulo = int(sumoffirstgradeweigh/11)
    print (firstgradeweighmodulo)
    calc1 = int(firstgradeweighmodulo*11)
    print (calc1)
    controlnumber1 = int(sumoffirstgradeweigh - calc1)
    print (controlnumber1)

    if (controlnumber1 == 10):
        print ("I astme kontrollnumber tuli 10, alustan II astme kontrolli")
        secondgradeweighsum = [a*b for a,b in zip(idArr, secondgrade)]
        print (secondgradeweighsum)
        sumofsecondgradeweigh = int(sum(secondgradeweighsum))
        print (sumofsecondgradeweigh)

        secondgradeweighmodulo = int(sumofsecondgradeweigh/11)
        print (secondgradeweighmodulo)
        calc2 = int(secondgradeweighmodulo*11)
        print (calc2)
        controlnumber2 = int(sumofsecondgradeweigh - calc2)
        print (controlnumber2)

        if (controlnumber2 == 10):
            controlnumber3 = 0
            print (controlnumber3)
            print ("II astme kontroll, peab olema null-TRUE: ", controlnumber3)
            return True
        elif (controlnumber2 != idArr[10]):
           print ("II astme kontrolli ei labinud, ei ole idkood-FALSE:", controlnumber2)
           return False
        else:
            print ("II astme kontroll-TRUE: ", controlnumber2)
            return True
    elif (controlnumber1 != idArr[10]):
        print ("I astme kontrolli ei labinud, ei ole idkood-FALSE", controlnumber1)
        return False
    else:
        print ("I astme kontroll-TRUE: ", controlnumber1)
        return True

#is_person_code_valid("49403136526")
is_person_code_valid("47605030299")
#is_person_code_valid("37605030299")
#is_person_code_valid("37810018540")

#peab kontrollima igat numbrit!!!!!
